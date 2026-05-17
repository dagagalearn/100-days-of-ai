import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
full_data = pd.read_csv(url)
full_data["Age"] = full_data["Age"].fillna(full_data["Age"].mean())
old_data, new_data = train_test_split(full_data,test_size=0.3,random_state=42)

print(full_data.isnull().sum())

from prefect import task, flow
import joblib

@task 
def combine_data(data_1,data_2):
  combined_data = pd.concat([data_1,data_2])
  return combined_data

@task
def process_data(data):
  data = data.drop(["Name","Ticket","Cabin","Embarked"],axis=1) # Keeping things simple
  data = pd.get_dummies(data, drop_first=True)
  return data

@task(retries=3, retry_delay_seconds=10)
def get_x_and_y(data):
  if data.isnull().sum().any():
    raise ValueError("found null values")
  else:
    X= data.drop(["Survived"], axis=1)
    y = data["Survived"]
  return X,y

@task 
def split_X_y(X,y):
  X_train, X_test, y_train, y_test = train_test_split(X,y)
  return X_train, X_test, y_train, y_test

@task
def train_model(X_train,y_train,X_test,y_test):
  model = RandomForestClassifier(n_estimators=100,max_depth=4)
  model.fit(X_train, y_train)
  score = model.score(X_test,y_test)
  return model, score

@task 
def decision_making(score_1, score_2,new_model):
  if score_2> score_1:
    joblib.dump(new_model,"new_model.joblib")
    return "Model updated"
  else:
    return "No changes made"

@flow(name="Combining all the steps")
def comp():
    data_1 = old_data
    data_2 = combine_data(old_data, new_data)

    data_1_processed = process_data(data_1)
    data_2_processed = process_data(data_2)

    X_d1, y_d1 = get_x_and_y(data_1_processed)
    X_d2, y_d2 = get_x_and_y(data_2_processed)

    X_d1_train, X_d1_test, y_d1_train, y_d1_test = split_X_y(X_d1,y_d1)
    X_d2_train, X_d2_test, y_d2_train, y_d2_test = split_X_y(X_d2,y_d2)

    old_model, score_1 = train_model(X_d1_train, y_d1_train, X_d1_test, y_d1_test)
    new_model, score_2 = train_model(X_d2_train, y_d2_train, X_d2_test, y_d2_test)

    decision_making(score_1,score_2,new_model)
    print("Done!")
  
if __name__ == "__main__":
  comp()




