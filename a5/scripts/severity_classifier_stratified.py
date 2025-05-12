from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Starting the Spark session
spark = SparkSession.builder.appName("WeightedSeverityClassifier").getOrCreate()

# Loading the dataset from the mounted volume
df = spark.read.csv("/data/severity_labeled_with_demographics.csv", header=True, inferSchema=True)
print(f"Loaded {df.count()} rows.")

# Converting the text label into a binary numeric label
df = df.withColumn("label", when(col("Severity") == "high", 1).otherwise(0))

# Defining numerical and categorical features to use in the model
numeric_features = [
    'Mortality Rate (%)', 'Incidence Rate (%)', 'Prevalence Rate (%)',
    'Healthcare Access (%)', 'Doctors per 1000', 'Hospital Beds per 1000',
    'Education Index', 'Per Capita Income (USD)', 'Urbanization Rate (%)'
]
categorical_features = ['Age Group', 'Gender']

# Indexing and encoding categorical variables so they can be used in the model
indexers = [StringIndexer(inputCol=col_name, outputCol=f"{col_name}_index", handleInvalid="keep")
            for col_name in categorical_features]
encoders = [OneHotEncoder(inputCol=f"{col_name}_index", outputCol=f"{col_name}_vec")
            for col_name in categorical_features]

# Combining all features into a single vector column
assembler_inputs = numeric_features + [f"{col}_vec" for col in categorical_features]
assembler = VectorAssembler(inputCols=assembler_inputs, outputCol="features")

# Splitting data by class label to preserve class balance in train and test sets
df_high = df.filter(col("label") == 1)
df_low = df.filter(col("label") == 0)

train_high, test_high = df_high.randomSplit([0.8, 0.2], seed=42)
train_low, test_low = df_low.randomSplit([0.8, 0.2], seed=42)

train = train_high.union(train_low)
test = test_high.union(test_low)

print(f"Training set size: {train.count()}, Test set size: {test.count()}")

# Computing class weights so the model doesn't favor the majority class
counts = train.groupBy("label").agg(count("*").alias("count")).collect()
total = sum(row["count"] for row in counts)
class_weights = {row["label"]: total / row["count"] for row in counts}
print(f"Computed class weights: {class_weights}")

# Assigning a weight column to the training data based on class weights
train = train.withColumn("classWeight", when(col("label") == 1, class_weights[1]).otherwise(class_weights[0]))

# Initializing the Random Forest classifier using class weights
rf = RandomForestClassifier(labelCol="label", featuresCol="features", weightCol="classWeight", numTrees=100, seed=42)

# Building the full ML pipeline
pipeline = Pipeline(stages=indexers + encoders + [assembler, rf])

# Fitting the model on the training data
model = pipeline.fit(train)

# Running predictions on the test set
predictions = model.transform(test)

# Evaluating the accuracy of the model
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Model Accuracy: {accuracy:.4f}")

# Displaying confusion matrix: counts of true/false positives/negatives
print("Confusion Matrix:")
predictions.groupBy("label", "prediction").count().orderBy("label", "prediction").show()


# Extracting Feature Importances
# Getting the trained RandomForest model from the pipeline
rf_model = model.stages[-1]  # Last stage is the RandomForestClassifier

# Getting feature importances as an array
importances = rf_model.featureImportances.toArray()

# These are the feature names used in the assembler
feature_names = assembler.getInputCols()

# Zipping them together
importance_list = list(zip(feature_names, importances))

# Sorting by importance (descending)
importance_list_sorted = sorted(importance_list, key=lambda x: x[1], reverse=True)

# Printing them 
print("\nFeature Importances:")
for feature, importance in importance_list_sorted:
    print(f"{feature}: {importance:.4f}")

