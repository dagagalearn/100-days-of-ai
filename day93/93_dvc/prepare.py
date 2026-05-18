import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data.csv")
data["Age"] = data["Age"].fillna(data["Age"].mean())

import joblib
import json

data = data.drop(["Name","Ticket","Cabin","Embarked"],axis=1) # Keeping things simple
data = pd.get_dummies(data, drop_first=True)

X= data.drop(["Survived"], axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = RandomForestClassifier(n_estimators=100,max_depth=4)
model.fit(X_train, y_train)
score = model.score(X_test,y_test)

with open("titanic_model.joblib","wb") as f:
    joblib.dump(model,f)

with open("accuracy_metrics.json", "w") as f:
    json.dump({"accuracy": score},f)

