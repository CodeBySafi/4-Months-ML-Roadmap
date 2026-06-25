import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

# --- Dummy Data: Software Bug Tracker ---
data_bugs = {
    'Bug_ID': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
    'Browser': ['Chrome', 'Firefox', 'Safari', 'Chrome', 'Safari', 'Firefox', 'Chrome', 'Safari'], # Nominal
    'Severity': ['Low', 'Critical', 'Medium', 'Medium', 'Critical', 'Low', 'Critical', 'Medium'], # Ordinal
    'Fix_Priority': ['Slow', 'Fast', 'Slow', 'Slow', 'Fast', 'Slow', 'Fast', 'Slow'] # Target
}
df_bugs = pd.DataFrame(data_bugs)
print("--- 1. Original Data ---")
print(df_bugs.head())

one_hot_encoding=pd.get_dummies(df_bugs,columns=[ 'Browser'],drop_first=True,dtype=int)
print(one_hot_encoding)

X=one_hot_encoding[[ 'Severity', 'Browser_Firefox', 'Browser_Safari']]
y=one_hot_encoding['Fix_Priority']

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.25, random_state=42, stratify=y
)

level=["Low", "Medium", "Critical"]

encoded=OrdinalEncoder(categories=[level])
X_train['Severity']=encoded.fit_transform(X_train[['Severity']])
X_test['Severity']=encoded.transform(X_test[['Severity']])
print(X_train)
print(X_test)