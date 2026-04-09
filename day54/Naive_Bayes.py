# Exercise: GaussianNB on iris

from sklearn.datasets import load_iris
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)
print(f"The GaussianNB model accuracy is: {(model.score(X_test, y_test)*100):.2f}%")
y_pred = model.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
sp_names = iris.target_names

plt.figure(figsize=(6,8))
sns.heatmap(cm,annot=True,cmap="Reds",xticklabels = sp_names,yticklabels = sp_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix on Iris")
plt.show()
