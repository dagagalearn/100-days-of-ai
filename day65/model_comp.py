# EXERCISE: Compare 5 algorithms performance.
# 1. Logistic Regression
# 2. SVM
# 3. Random Forest
# 4. Decision Trees
# 5. XGBoost
# The dataset we're gonna use: Iris Dataset

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd




# Data Preparation
data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=5)

# 1. Logistic Regression
params_grid={
    "max_iter": [100, 200, 500, 1000, 2500, 5000]
}
model_1 = LogisticRegression()
grid_search_cv_1 = GridSearchCV(model_1, param_grid=params_grid, cv=5)
grid_search_cv_1.fit(X_train, y_train)
print(f"The best parameters for the LogisticRegression are: {grid_search_cv_1.best_params_}")
print(f"The best score for the LogisticRegression is: {grid_search_cv_1.best_score_:.2f}")
# The best parameters for the LogisticRegression are: {'max_iter': 100}
# The best score for the LogisticRegression is: 0.97

# 2. SVM
params_grid_svm = {
    'C': [0.1, 1, 10, 100, 1000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
    'kernel': ['rbf','linear','poly']
}

model_2 = SVC()
grid_search_cv_2 = GridSearchCV(model_2, param_grid=params_grid_svm,cv=5)
grid_search_cv_2.fit(X_train, y_train)
print(f"The best parameters for the SVM are: {grid_search_cv_2.best_params_}")
print(f"The best score for the SVM is: {grid_search_cv_2.best_score_:.2f}")
# The best parameters for the SVM are: {'C': 0.1, 'gamma': 0.1, 'kernel': 'poly'}
# The best score for the SVM is: 0.99

# 3. Random Forest
model_3 = RandomForestClassifier()
params_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
}

grid_search_cv_3 = GridSearchCV(model_3, param_grid=params_grid_rf,cv=5)
grid_search_cv_3.fit(X_train, y_train)
print(f"The best parameters for the RandomForest are: {grid_search_cv_3.best_params_}")
print(f"The best score for the Random Forest is: {grid_search_cv_3.best_score_:.2f}")

# The best parameters for the RandomForest are: {'max_depth': None, 'n_estimators': 100}
# The best score for the Random Forest is: 0.96


# 4. Decision Tree
model_4 = DecisionTreeClassifier()
params_grid_dt = {
    'max_depth': [None, 5, 10, 20],
}
grid_search_cv_4 = GridSearchCV(model_4, param_grid=params_grid_dt,cv=5)
grid_search_cv_4.fit(X_train, y_train)
print(f"The best parameters for the DecisionTree are: {grid_search_cv_4.best_params_}")
print(f"The best score for the DecisionTree is: {grid_search_cv_4.best_score_:.2f}")

# The best parameters for the DecisionTree are: {'max_depth': 5}
# The best score for the DecisionTree is: 0.96

# 5. XGboost
model_5 = XGBClassifier()
params_grid_xgb = {
    'n_estimators': [100, 500, 1000],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'gamma': [0,0.1,0.2]
}

grid_search_cv_5 = GridSearchCV(model_5, param_grid=params_grid_xgb, cv=5)
grid_search_cv_5.fit(X_train, y_train)
print(f"The best parameters for the XGboost are: {grid_search_cv_5.best_params_}")
print(f"The best score for the XGboost is: {grid_search_cv_5.best_score_:.2f}")

# The best parameters for the XGboost are: {'gamma': 0, 'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 100}
# The best score for the XGboost is: 0.94


# Final Words

""" In this case the winner is of course, SVM. For quite a few reasons
one being the model had a lot of parameters for the GridSearchCV. And the data
might be near perfect for the model, SVM """

performance_data = {
    'LogisticRegression' : ["{'max_iter': 100}", 0.97,grid_search_cv_1.score(X_test, y_test)],
    'SVM' : ["{'C': 0.1, 'gamma': 0.1, 'kernel': 'poly'}", 0.99,grid_search_cv_2.score(X_test, y_test)],
    'RandomForest' : ["{'max_depth': None, 'n_estimators': 100}", 0.96,grid_search_cv_3.score(X_test, y_test)],
    'DecisionTree' : ["{'max_depth': 5}", 0.96,grid_search_cv_4.score(X_test, y_test)],
    'XGBoost' : ["{'gamma': 0, 'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 100}", 0.94,grid_search_cv_5.score(X_test, y_test)],
}

df = pd.DataFrame(performance_data,index=["Best Param(s)","Best Score","Test Score"])

df

