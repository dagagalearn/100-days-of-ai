# exercise: compare linear and rbf kernel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

iris = load_iris()
X = iris.data
y = iris.target
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=101)

classifier = SVC()
param_grid = {
    "C": [0.1,1,5,10],
    "gamma": ["auto","scale",1,10],
    "kernel" : ["rbf","linear","poly"]
}

gs_md = GridSearchCV(param_grid = param_grid, estimator=classifier,cv=5)
result = gs_md.fit(X_train, y_train)

print(f"The best training score is {result.best_score_} and is scored by {result.best_params_}") 
#The best score is 0.9833333333333334 and is scored by {'C': 1, 'gamma': 'auto', 'kernel': 'linear'}

model = SVC(gamma="auto", C=1, kernel="linear")
model.fit(X_train, y_train)
lnr_score = model.score(X_test, y_test) 

model_rbf =  SVC(gamma="auto", C=1, kernel="rbf")
model_rbf.fit(X_train, y_train)
rbf_score = model_rbf.score(X_test, y_test) 

print(f"The accuracy for linear kernel is {lnr_score} and for rbf: {rbf_score}")




