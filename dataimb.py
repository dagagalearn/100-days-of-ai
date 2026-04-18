from sklearn.datasets import make_classification
import pandas as pd
X, y = make_classification(n_samples=10_000,
                           n_features=30,
                           n_clusters_per_class=1,
                           weights=[0.99],flip_y=0)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.25,
                                                    random_state=42)
pd.Series(y_train).value_counts().plot.pie(autopct="%2f")


rfm = RandomForestClassifier(random_state=42)
rfm.fit(X_train, y_train)
y_pred = rfm.predict(X_test)
print(classification_report(y_test, y_pred))


from imblearn.over_sampling import SMOTE

sm = SMOTE()
X_res, y_res = sm.fit_resample(X_train, y_train)
smote_rmf = RandomForestClassifier(random_state=42)
smote_rmf.fit(X_res, y_res)
y_pred = smote_rmf.predict(X_test)
print(classification_report(y_test, y_pred))
pd.Series(y_res).value_counts().plot.pie(autopct="%2f")



from imblearn.ensemble import BalancedRandomForestClassifier
brmf = BalancedRandomForestClassifier(n_estimators=100,random_state=42)
brmf.fit(X_train, y_train)
y_pred = brmf.predict(X_test)

print(classification_report(y_test, y_pred))

from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X_train, y_train)
rfm.fit(X_res, y_res)
y_pred = rfm.predict(X_test)
print(classification_report(y_test, y_pred))
pd.Series(y_res).value_counts().plot.pie(autopct="%2f")

# Hence we solved the imbalanced data by two methods (SMOTE and RandomUnderSampler)


