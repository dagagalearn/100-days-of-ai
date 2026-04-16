import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

train_data = pd.read_csv("house_prices/train.csv")
test_data = pd.read_csv("house_prices/test.csv")

corr_matrix = train_data.corr(numeric_only=True)

cols = corr_matrix.nlargest(10,'SalePrice')['SalePrice'].index
plt.figure(figsize=(10,8))
sns.heatmap(train_data[cols].corr(), annot=True,cmap="coolwarm")
plt.show()

plt.scatter(train_data['GrLivArea'],train_data['SalePrice'])
plt.xlabel("Living Area")
plt.ylabel("Sale Price")
plt.show()


train_data=train_data.drop(train_data[(train_data['GrLivArea']>4000) & (train_data['SalePrice']<300000)].index)


train_data.head()


plt.scatter(train_data['GrLivArea'],train_data['SalePrice'])
plt.xlabel("Living Area")
plt.ylabel("Sale Price")
plt.show()


missing_data = train_data.isnull().sum().sort_values(ascending=False)

missing_data.head(12)


cols_to_fill_none = ["PoolQC","MiscFeature","Alley","Fence",
                     "FireplaceQu","GarageType",
                     "GarageFinish","GarageQual","GarageCond",
                     "BsmtQual","BsmtFinType1","BsmtFinType2"]



for col in cols_to_fill_none:
    train_data[col]=train_data[col].fillna("None")


train_data["GarageArea"]=train_data["GarageArea"].fillna(0)


train_data["LotFrontage"]=train_data.groupby("Neighborhood")["LotFrontage"].transform(lambda x: x.fillna(x.median()))

train_data = train_data.drop(["Utilities"],axis=1)


train_data["SalePrice"]=np.log1p(train_data["SalePrice"])
quality_map = {
    "Ex" : 5,
    "Gd": 4,
    "TA":3,
    "Fa":2,
    "Po": 1,
    "None": 0
}

cols_to_map = ["ExterQual","ExterCond","BsmtQual","BsmtCond","HeatingQC","KitchenQual","FireplaceQu","GarageQual","GarageCond","PoolQC"]


for col in cols_to_map:
    train_data[col]=train_data[col].map(quality_map)
    test_data[col]=test_data[col].map(quality_map)

train_data = pd.get_dummies(train_data)
test_data = pd.get_dummies(test_data)

train_data["TotalArea"] = train_data["TotalBsmtSF"] + train_data["1stFlrSF"] + train_data["2ndFlrSF"]
test_data["TotalArea"] = test_data["TotalBsmtSF"] + test_data["1stFlrSF"] + test_data["2ndFlrSF"]


y= train_data["SalePrice"]
X = train_data.drop(["Id","SalePrice"],axis=1)
train_data, test_data = train_data.align(test_data,join="left",axis=1)

test_data = test_data.fillna(0)
train_data = train_data.fillna(0)


from sklearn.model_selection import train_test_split


X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


from sklearn.linear_model import Lasso

model_lasso = Lasso(alpha=0.0005)
model_lasso.fit(X_train, y_train)


from sklearn.metrics import mean_squared_error 


preds = model_lasso.predict(X_test)
print(f"RMSE score: {np.sqrt(mean_squared_error(y_test,preds))}")

X_test_l = test_data.drop(["Id"],axis=1)

X_test_l = X_test_l.reindex(columns=X.columns,fill_value=0)
X_test_l = X_test_l.fillna(0)
final_pred_log = model_lasso.predict(X_test)


final_pred_log = model_lasso.predict(X_test_l)
final_pred_dol = np.expm1(final_pred_log)

submission=pd.DataFrame({
    "Id" : test_data["Id"],
    "SalePrice": final_pred_dol
})

submission.to_csv("submission_house_pr.csv",index=False)


