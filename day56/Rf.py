from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

digits = load_digits()
digits = pd.DataFrame(digits.data)
digits["target"] = load_digits().target

digits.head()

X = digits.drop(["target"], axis = 1)
y = digits["target"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)

clf_model = RandomForestClassifier(n_estimators=100)
clf_model.fit(X_train, y_train)
print(f"The score is: {clf_model.score(X_test, y_test)}")

y_pred = clf_model.predict(X_test)
cm = confusion_matrix(y_test,y_pred)

plt.figure(figsize=(12,8))
plt.title("Confusion Matrix Plot")
sns.heatmap(cm,annot=True,cmap="Blues",fmt="d")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()
