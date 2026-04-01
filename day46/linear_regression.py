import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv"
house_data = pd.read_csv(url)

house_data.columns = house_data.columns.str.strip()

model = LinearRegression()


X = house_data[['SqFt', 'Bedrooms', 'Bathrooms', 'Offers']]
y = house_data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)


predictions = model.predict(X_test)
accuracy_score = model.score(X_test, y_test)

print(f"R^2 Score: {accuracy_score}")
