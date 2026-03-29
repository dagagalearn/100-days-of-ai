
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
X = titanic[['Age','Fare']].fillna(titanic[['Age','Fare']].median())
y = titanic['Survived']

scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

int(np.round(X_train_scaled.mean())) # outputs 0 
int(np.round(X_train_scaled.std())) # outputs 1 (hence the data is scaled)

model = LogisticRegression()
model.fit(X_train,y_train)
model.predict(X_test)
model.score(X_test,y_test) # without using StandardScaler accuracy of 60.3%


model.fit(X_train_scaled,y_train)
model.predict(X_train_scaled)
model.score(X_test_scaled, y_test) #Oops! again the same, No worries: don't think StandardScaler is bad at its job, this happened because of my low decision variable(Age+Fare)



