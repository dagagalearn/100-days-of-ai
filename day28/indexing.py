import pandas as pd

# 1. Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana', 'Eli'],
    'Score': [95, 80, 65, 92, 88],
    'Passed': [True, True, False, True, True]
}
df = pd.DataFrame(data)

# 2. Define a condition (The "Mask")
# Let's find students who scored above 90
condition = df['Score'] > 90

# 3. Apply the filter
top_students = df[condition]

print(top_students)
