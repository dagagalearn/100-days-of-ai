import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(URL)


features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
df = df[features + ['Survived']].dropna()

X = df[features]
y = df['Survived']


model = LogisticRegression()
model.fit(X, y)


joblib.dump(model, "titanic_model.pkl")

print("Model trained on 5 features and saved as titanic_model.pkl")
#Just to check our work on. Not trained well
