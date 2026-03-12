import pandas as pd

grades = {
"name": ["Tola Chala","Sara Bekele","Abel Tesfaye","Hana Desta","Noah Girma"],
"math":[100,95,88,92,97],
"physics":[100,90,85,94,93],
"chemistry":[98,91,84,90,95],
"biology":[96,89,80,93,92],
"english":[97,94,87,91,96]
}

df = pd.DataFrame(grades)

print("\n The datas")
print(df)

print("\n the first 3 datas ")
print(df.head(3))

print("\n The last 3 datas")
print(df.tail(3))

print("\n Those having average greater than 90")
print(df[df.iloc[:,1:].mean(axis=1)>90])

print("\n The data statistics")
print(df.describe())
