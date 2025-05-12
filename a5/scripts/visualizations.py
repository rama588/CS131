import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv("severity_labeled_with_demographics.csv")
df.columns = df.columns.str.strip()  # Cleaning column names


# Violin Plot of Prevalence Rate (%) by Severity

plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x="Severity", y="Prevalence Rate (%)", hue="Severity", split=False, inner="box", palette="pastel")
plt.title("Distribution of Prevalence Rate (%) by Severity")
plt.xlabel("Severity")
plt.ylabel("Prevalence Rate (%)")
plt.tight_layout()
plt.savefig("prevalence_by_severity_violin_hue.png", dpi=300)
plt.close()


# Hexbin Plot of Mortality vs Healthcare Access (by Severity)

fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True)

# Adding extra space to the right for the colorbar
plt.subplots_adjust(wspace=0.25, right=0.88)

last_hb = None

for i, severity in enumerate(["low", "high"]):
    subset = df[df["Severity"] == severity]

    hb = axes[i].hexbin(x=subset["Healthcare Access (%)"], y=subset["Mortality Rate (%)"], gridsize=30, cmap="coolwarm", mincnt=1)
    axes[i].set_title(f"{severity.capitalize()} Severity")
    axes[i].set_xlabel("Healthcare Access (%)")
    axes[i].set_ylabel("Mortality Rate (%)")
    axes[i].tick_params(axis='y', which='both', labelleft=True)
    last_hb = hb

# Placing colorbar to the far right
cb = fig.colorbar(last_hb, ax=axes, orientation='vertical', fraction=0.035, pad=0.02)
cb.set_label("Number of Records")

plt.suptitle("Hexbin: Mortality vs Healthcare Access by Severity", fontsize=14)
plt.savefig("hexbin_mortality_vs_access_by_severity.png", dpi=300)
plt.close()


print("Plots have been saved:")
print("- prevalence_by_severity_violin_hue.png")
print("- hexbin_mortality_vs_access_by_severity.png")
