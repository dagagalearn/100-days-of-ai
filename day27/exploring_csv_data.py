import pandas as pd

df = pd.read_csv("data.csv")

print("\nFirst 3 rows")
print(df.head(3))

print("\nLast 3 rows")
print(df.tail(3))

print("\nDataset shape")
print(df.shape)

print("\nColumn names")
print(df.columns)

print("\nDataset info")
print(df.info())

print("\nStatistics")
print(df.describe())

print("\nMissing values")
print(df.isnull().sum())

print("\nRandom sample")
print(df.sample(5))

print("\nCorrelation matrix")
print(df.corr())

df.to_excel("data.xlsx", index=False)
