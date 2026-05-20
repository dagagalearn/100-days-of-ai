import pandas as pd
# LabelEncoder is no longer needed as we'll handle 'Sex' directly and drop 'Embarked'
import xgboost as xgb
import joblib # Import joblib for saving the model

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
data= pd.read_csv(url)

# Identify numerical columns for median imputation
cols_for_median_fill = ["Age", "Fare", "SibSp", "Parch"]
medians = data[cols_for_median_fill].median()

def clean_and_prepare_features(df, median_values):
    # Drop columns not needed for the model or the API input
    # This includes 'PassengerId', 'Name', 'Ticket', 'Cabin', and 'Embarked'
    df = df.drop(["PassengerId", "Name", "Ticket", "Cabin", "Embarked"], axis=1, errors='ignore')
    
    # Fill missing numerical values with their medians
    df.fillna(median_values, inplace=True)
    
    # Create 'Sex_male' feature (0 for female, 1 for male) to match FastAPI model
    df['Sex_male'] = df['Sex'].apply(lambda x: 1 if x == 'male' else 0)
    # Drop the original 'Sex' column
    df = df.drop('Sex', axis=1)

    # Ensure Pclass, SibSp, Parch are of integer type if they became float due to NaNs or other operations
    for col in ['Pclass', 'SibSp', 'Parch']:
        if col in df.columns:
            df[col] = df[col].astype(int)

    return df

# Apply the enhanced cleaning and feature preparation to the dataset
data = clean_and_prepare_features(data, medians)

# Define features for X, explicitly ordering them as expected by the FastAPI Passenger model
feature_columns = [
    'Pclass',
    'Age',
    'SibSp',
    'Parch',
    'Fare',
    'Sex_male'
]

# Ensure X only contains the desired features in the correct order
X = data[feature_columns]
y = data["Survived"]

clf = xgb.XGBClassifier(n_estimators=100,
                        max_depth=4,
                        learning_rate=0.05,
                        subsample=0.8,
                        colsample_bytree=0.8,
                        eval_metric="logloss",
                        random_state=42
                       )

clf.fit(X,y)

# Save the trained model
joblib.dump(clf, "titanic_model.joblib")
print("Model saved to titanic_model.joblib")
