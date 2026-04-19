# EXERCISE: Pipeline with GridSearchCV.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)


data = data.drop(["Name", "PassengerId","Ticket","Cabin"],axis=1)
data["Embarked"] = data["Embarked"].fillna("U")
data = pd.get_dummies(data, drop_first=True)
X = data.drop(["Survived"],axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

pipe = Pipeline([
    ('imputer', SimpleImputer()),
    ('model', RandomForestClassifier(random_state=101))
])

params_grid = {
    "imputer__strategy": ["mean","median"],
    "model__max_depth": [10,20,None],
    "model__n_estimators": [10,100,50]
}

grid_search = GridSearchCV(pipe, param_grid=params_grid, cv=5)


grid_search.fit(X_train, y_train)

print(f"The best parameters are {grid_search.best_params_}\nThe best score is {(grid_search.best_score_)*100:.2f}%\nThe model score is: {grid_search.score(X_test,y_test)*100:.2f}")

