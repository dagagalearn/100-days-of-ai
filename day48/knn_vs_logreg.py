# packing my tools
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# pulling the data down
iris = load_iris()

# Splitting train and test data + scaling the data
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2, 
    random_state=42,
    stratify=y
)

# KNN pipeline
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

knn_pipeline.fit(X_train, y_train)
knn_score = knn_pipeline.score(X_test, y_test)

# Logistic Regression pipeline
logreg_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression())
])

logreg_pipeline.fit(X_train, y_train)
logreg_score = logreg_pipeline.score(X_test, y_test)

print("KNN Accuracy:", knn_score)
print("Logistic Regression Accuracy:", logreg_score)
