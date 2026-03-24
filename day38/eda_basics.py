import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

columns = ['age', 'operation_year', 'axillary_nodes', 'survival_status']
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/haberman.csv"
df = pd.read_csv(url, names=columns)

print("--- Shape of Data ---")
print(df.shape)  

print("\n--- Survival Counts ---")
print(df['survival_status'].value_counts()) 


print("\n--- Summary Statistics ---")
print(df.describe())


sns.FacetGrid(df, hue="survival_status", height=5) \
    .map(sns.kdeplot, "axillary_nodes") \
   .add_legend()
plt.title("Distribution of Axillary Nodes by Survival Status")

df['survival_status'] = df['survival_status'].map({1: "Survived >5yrs", 2: "Died <5yrs"})

sns.set_style("whitegrid")
sns.pairplot(df, hue="survival_status", height=3)

plt.show()
