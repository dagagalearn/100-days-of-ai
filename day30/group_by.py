import pandas as pd
sales_data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "date": [
        "2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-03",
        "2026-03-03", "2026-03-04", "2026-03-04", "2026-03-05", "2026-03-05"
    ],
    "product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse"
    ],
    "category": [
        "Electronics", "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories", "Electronics", "Electronics", "Accessories"
    ],
    "price": [1200, 25, 75, 300, 1150, 20, 70, 1250, 320, 22],
    "quantity": [2, 10, 5, 3, 1, 8, 6, 2, 4, 7],
    "region": [
        "East", "West", "East", "North", "South",
        "East", "West", "South", "North", "East"
    ],
    "sales_rep": [
        "Alice", "Bob", "Alice", "David", "Eva",
        "Bob", "Alice", "Eva", "David", "Bob"
    ]
}

df = pd.DataFrame(sales_data)

# Print the original data
print(df)
# Find the average price
print(df.groupby('product').agg({'price': 'mean','quantity':'sum'}))
# Tranform the data
print(df.groupby('product')['price'].transform('mean'))
# Filter the data having columns wwith price >=1000
print(df[df['price']>=1000])
