import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Loading the dataset
df = pd.read_csv("covid_only.csv")
print("Initial dataset shape:", df.shape)

# Dropping columns that are not needed for this analysis
cols_to_drop = ["Disease Category", "DALYs", "Recovery Rate (%)", "Average Treatment Cost (USD)", "Availability of Vaccines/Treatment", "Treatment Type", "Population Affected"]

# Only dropping columns that exist to avoid errors
df.drop(columns=[col for col in cols_to_drop if col in df.columns], inplace=True)

# These are the features we are using to define our severity score
severity_features = ["Mortality Rate (%)", "Incidence Rate (%)", "Prevalence Rate (%)", "Healthcare Access (%)"]

# Creating a copy of the dataframe before scaling
df_scaled = df.copy()

# Normalizing the severity features between 0 and 1
scaler = MinMaxScaler()
df_scaled[severity_features] = scaler.fit_transform(df[severity_features])

# Computing a custom severity score
# Note: We subtract healthcare access to indicate worse severity with lower access
df_scaled["Severity_Score"] = (df_scaled["Mortality Rate (%)"] + df_scaled["Incidence Rate (%)"] + df_scaled["Prevalence Rate (%)"] + (1 - df_scaled["Healthcare Access (%)"]))

# Seting a threshold at the 75th percentile to label the top 25% as 'high' severity
severity_threshold = df_scaled["Severity_Score"].quantile(0.75)
df_scaled["Severity"] = np.where(df_scaled["Severity_Score"] > severity_threshold, "high", "low")

# Dropping the helper column after labeling
df_final = df_scaled.drop(columns=["Severity_Score"])

# Saving the final dataset with the new 'Severity' label
df_final.to_csv("severity_labeled_with_demographics.csv", index=False)

# Printing summary
print("\nLabeled dataset saved as 'severity_labeled_with_demographics.csv'")
print("Final shape:", df_final.shape)
print("\nSeverity distribution:\n", df_final["Severity"].value_counts())
print("\nPreview of the labeled data:")
print(df_final.head())
