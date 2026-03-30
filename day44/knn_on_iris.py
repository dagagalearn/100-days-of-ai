# packing my tools
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# pulling the data down
iris = load_iris()

# Splitting train and test data + scaling the data
X, y = iris.data, iris.target
X_train, X_test, y_train,y_test = train_test_split(X,y,
                                                   test_size=0.2, 
                                                   random_state=42,
                                                   stratify=y)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

pipeline.fit(X_train,y_train)

pipeline.predict(X_test)
pipeline.score(X_test,y_test)
