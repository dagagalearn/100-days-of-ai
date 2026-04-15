import pandas as pd
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb

data= pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")

pass_id_vals = test["PassengerId"].values

cols = ["SibSp","Parch","Fare","Age"]
medians = data[cols].median()

def clean(df,fill_values):
    df = df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
    df.fillna(fill_values,inplace=True)
    df.fillna({"Embarked": "U"},inplace=True)
    return df

data=clean(data,medians)
test=clean(test,medians)

le = LabelEncoder()

cols = ["Sex","Embarked"]
for col in cols:
    data[col] = le.fit_transform(data[col])
    test[col] = le.transform(test[col])


clf = xgb.XGBClassifier(n_estimators=100,
                        max_depth=4,
                        learning_rate=0.05,
                        subsample=0.8,
                        colsample_bytree=0.8,
                        eval_metric="logloss", 
                        random_state=42  
                       )

X = data.drop(["Survived"],axis=1)
y = data["Survived"]

# I am not using train_test_split because I want my model to use more data to  perform more in the test data
clf.fit(X,y) 
y_pred = clf.predict(test)

df = pd.DataFrame({
    "PassengerId": pass_id_vals,
    "Survived": y_pred,
})

df.to_csv("submission_file_final.csv",index=False)
