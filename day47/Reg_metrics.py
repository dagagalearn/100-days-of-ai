from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

X = np.array([1,2,3,4,6,8,19,20,25,24,26,27,60,62,65]).reshape(-1,1)
y = np.array([2,4,7,9,11,16,38,39,49,48,52,55,122,124,130])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(model.score(X_test, y_test))

MAE = mean_absolute_error(y_test, y_pred)
print(MAE)

MSE = mean_squared_error(y_test, y_pred)
print(MSE)

RMSE = root_mean_squared_error(y_test,y_pred)
print(RMSE)

R2 = r2_score(y_test,y_pred)
print(R2)
