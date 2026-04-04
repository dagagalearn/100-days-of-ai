from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y)
clf = DecisionTreeClassifier(max_depth=3, random_state=42)

clf.fit(X_train, y_train)
clf.predict(X_test)
model_score = clf.score(X_test, y_test)

plt.figure(figsize=(12,8))
plot_tree(
    clf,
    feature_names = iris['feature_names'],
    filled = True,
    rounded = True,
    fontsize=12
)

plt.show()
exp_txt = export_text(clf,
                      feature_names=iris['feature_names'], 
                      class_names = list(iris['target_names']),
                      decimals = 1,
                      spacing = 4)
print(exp_txt)
print(f"Model's score is: {model_score}")

# Predicting New Datapoint

new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = clf.predict(new_flower)

predicted_name = iris['target_names'][prediction][0]
print(f"The model predicted the new flower is: {predicted_name} with confidence score of: {clf.predict_proba(new_flower)} ") 
