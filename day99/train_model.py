from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import json

data = pd.read_csv("data.csv")

# Data Processing 
data = data.drop(["PassengerId","Name","Ticket","Cabin","Embarked"], axis =1)
data = pd.get_dummies(data, dtype=int)
X = data.drop("Survived", axis =1)
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training model
model = RandomForestClassifier(n_estimators=90, max_depth=5,min_samples_leaf=6,min_samples_split=3)
model.fit(X_train, y_train)
model.score(X_test,y_test)


with open("titanic_model.joblib","wb") as f:
    joblib.dump(model,f)
print("titanic_model.joblib saved!")
with open("model_features.joblib","wb") as f:
    joblib.dump(X.columns.tolist(),f)
print("model_features.joblib saved!")
with open("scaler.joblib","wb") as f:
  joblib.dump(scaler,f)
print("scaler.joblib saved!")

# check
loaded_model = joblib.load("titanic_model.joblib")
loaded_features = joblib.load("model_features.joblib")
loaded_scaler = joblib.load("scaler.joblib")

print(f"Features: {len(loaded_features)}: {loaded_features}")
print(f"Model accuracy: {loaded_model.score(X_test,y_test)}")

with open("metrics.json","w") as f:
    json.dump({"accuracy":model.score(X_test,y_test)},f)

print("Saved!")
