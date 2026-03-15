import pandas as pd
dataset = {
    "student": ["Alem", "Sara", "Dawit", "Hana", "Noah", "Liya"],
    "math_score": [78, None, 92, 85, None, 88],
    "physics_score": [None, 81, 95, None, 76, 90],
    "study_hours": [3, 4, None, 5, 2, None],
    "passed_exam": [True, True, True, None, False, True]
}

df = pd.DataFrame(dataset)
print(df.isna().sum()) # Print the NaN values
df.fillna({
    "math_score": df["math_score"].mean(),
"physics_score": df["physics_score"].mean(),
"study_hours": df["study_hours"].mean(),
    "passed_exam": False

},inplace=True)
print(df)
