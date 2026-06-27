import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data_lib = {
    'Student_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'Books_Borrowed_So_Far': [2, 15, 45, 5, 22, 1, 30, 12], 
    'Pending_Fine_PKR': [0, 500, 2500, 100, 1200, 0, 5000, 300], 
    'Days_To_Return': [2, 5, 12, 3, 7, 1, 15, 4] 
}
df_lib = pd.DataFrame(data_lib)
print("--- 1. Original Data ---")
print(df_lib.head())

X=df_lib[['Books_Borrowed_So_Far','Pending_Fine_PKR']]
y=df_lib['Days_To_Return']

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.25, random_state=42
)

std=StandardScaler()
x_train_std=std.fit_transform(X_train[['Books_Borrowed_So_Far','Pending_Fine_PKR']])
x_test_std=std.transform(X_test[['Books_Borrowed_So_Far','Pending_Fine_PKR']])

df_X_train=pd.DataFrame(x_train_std,columns=X_train.columns,index=X_train.index)
df_X_test=pd.DataFrame(x_test_std,columns=X_test.columns,index=X_test.index)
print(df_X_train)

print(df_X_test)
