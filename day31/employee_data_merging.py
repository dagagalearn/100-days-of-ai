import pandas as pd
employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "department_id": [1, 2, 1, 3, 2],
    "salary": [60000, 50000, 70000, 65000, 52000]
}

departments = {
    "department_id": [1, 2, 3, 4],
    "department_name": ["HR", "Engineering", "Marketing", "Finance"],
    "manager": ["John", "Sara", "Mike", "Anna"]
}


df_employee = pd.DataFrame(employees)
df_department = pd.DataFrame(departments)

merged_data = pd.merge(df_employee,df_department,on="department_id")
# The first data
print(df_employee)
# second data 
print(df_department)
# merged data 
print(merged_data)
# Printing other merges
print(pd.merge(df_employee,df_department,how="outer",indicator=True)) # gives the union of the two
print(pd.merge(df_employee,df_department,how="inner")) # intersection of the two
print(pd.merge(df_employee,df_department,how="left"))
print(pd.merge(df_employee,df_department,how="right"))
