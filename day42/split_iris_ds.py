from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

x_train , x_test, y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=67,stratify=y)
print(f"The length of x_train: {len(x_train)}")
print(f"The length of y_train: {len(y_train)}")
print(f"The length of x_test: {len(x_test)}")
print(f"The length of y_test: {len(y_test)}")

# The ration len(x_train)/len(x) = 0.8 and len(x_test)/len(y_test)
