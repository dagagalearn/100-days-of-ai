# Exercise: your first XGBoost model
from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = XGBClassifier(n_estimators=100, learning_rate=0.01,max_depth=3)
model.fit(X_train, y_train)
print(f"The model accuracy: {model.score(X_test, y_test)}")
