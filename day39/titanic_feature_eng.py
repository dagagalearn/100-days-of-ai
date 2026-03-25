import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("titanic")

df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df = df.drop(columns=["deck", "alive", "who", "adult_male", "class"])

df["sex"] = df["sex"].map({"male": 1, "female": 0})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

df["family_size"] = df["sibsp"] + df["parch"] + 1
df["is_alone"] = np.where(df["family_size"] == 1, 1, 0)
df["fare_per_person"] = df["fare"] / df["family_size"]

df["title"] = df["name"].str.extract('([A-Za-z]+)\.', expand=False)
rare_titles = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
df["title"] = df["title"].replace(rare_titles, 'Rare')
title_map = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Rare': 4}
df["title"] = df["title"].map(title_map)

df["age_group"] = pd.cut(df["age"], bins=[0, 12, 18, 35, 60, 80], labels=[0, 1, 2, 3, 4])
df["fare_group"] = pd.qcut(df["fare"], 4, labels=[0, 1, 2, 3])
df["fam_class"] = df["family_size"] * df["pclass"]

print(df.head())
print(df.info())
