# Exercise: Tune KNN hyperparameters
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=206)

knn = KNeighborsClassifier()

param_grid = {
    'n_neighbors' : [1,3,5,7,9,11,13,15,17]
}

param_dist = {
    'n_neighbors' : [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47]
}

grid_search = GridSearchCV(estimator=knn, param_grid = param_grid, cv=5)
result = grid_search.fit(X_train, y_train)
print(f"The best param is: {result.best_params_}, and the best score is: {result.best_score_}")


# Optional but
randomized_search_cv = RandomizedSearchCV(estimator=knn, param_distributions = param_dist, cv=5, n_iter=20)
result = randomized_search_cv.fit(X_train, y_train)
print(f"The best param is: {result.best_params_}, and the best score is: {result.best_score_}")
