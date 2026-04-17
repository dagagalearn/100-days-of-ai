# EXERCISE: Save/Load model using joblib

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pickle

url = "https://raw.githubusercontent.com/ywchiu/riii/refs/heads/master/data/house-prices.csv"
data = pd.read_csv(url)
print(data.head(5))


plt.scatter(data["SqFt"],data["Price"])
plt.xlabel("SqFt")
plt.ylabel("Price")
plt.title("SqFt vs Price Plot")
plt.show()

data = pd.get_dummies(data,drop_first=True)
print(data.head(5))



X = data.drop(["Price","Home"],axis=1)
y = data["Price"]
linear_regressor = LinearRegression()
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=67)
linear_regressor.fit(X_train, y_train)

linear_regressor.score(X_test, y_test)

# Saving the Model as a file and loading it for later use

joblib.dump(linear_regressor, "model_1")
# Using the saved model
joblib_model = joblib.load("model_1")
print((joblib_model.predict(X_test) == linear_regressor.predict(X_test)).all()) # np.True_

# Doing the same thing using pickles
with open("model_2", "wb") as f:
    pickle.dump(linear_regressor,f)

# Using pickle data
with open("model_2", "rb") as f:
    pickle_model = pickle.load(f)

print((pickle_model.predict(X_test) == linear_regressor.predict(X_test)).all()) # np.True_
