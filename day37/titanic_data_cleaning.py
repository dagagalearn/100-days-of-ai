import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df = df.drop(columns=["deck", "alive", "who", "adult_male", "class"])

df["sex"] = df["sex"].map({"male": 1, "female": 0})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

df["family_size"] = df["sibsp"] + df["parch"] + 1

print(df.head())
print(df.info())
