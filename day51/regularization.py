from sklearn.linear_model import Ridge, Lasso, ElasticNet, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
data_set = pd.read_csv(url)

data_encoded = pd.get_dummies(data_set, drop_first=True)

X = data_encoded.drop(columns=["charges"])
y = data_encoded["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


ridge_model = Ridge(alpha=10.0) 
ridge_model.fit(X_train_scaled, y_train)
print(f"Ridge Score: {ridge_model.score(X_test_scaled, y_test)}")


lasso_model = Lasso(alpha=100.0)
lasso_model.fit(X_train_scaled, y_train)
print(f"Lasso Score: {lasso_model.score(X_test_scaled, y_test)}")

normal_reg = LinearRegression()
normal_reg.fit(X_train_scaled, y_train)
print(f"Standard LinearRegression Score(without regularization): {normal_reg.score(X_test_scaled, y_test)}")

# Ridge Score: 0.7830200444609896
# Lasso Score: 0.7806320248423892
# Standard LinearRegression Score(without regularization): 0.7835929767120722
