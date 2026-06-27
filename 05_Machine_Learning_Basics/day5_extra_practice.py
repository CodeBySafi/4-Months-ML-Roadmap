import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# --- Dummy Data: Library Book Returns ---
data_library = {
    'Student_ID': ['S-01', 'S-02', 'S-03', 'S-04', 'S-05', 'S-06', 'S-07', 'S-08'],
    'Department': ['SE', 'CS', 'SE', 'IT', 'CS', 'IT', 'SE', 'CS'], # Nominal
    'Book_Category': ['Database', 'Programming', 'DLD', 'Database', 'DLD', 'Programming', 'Programming', 'Database'], # Nominal
    'Return_Status': ['On-Time', 'Late', 'On-Time', 'Late', 'On-Time', 'On-Time', 'Late', 'On-Time'] # Target
}
df_library = pd.DataFrame(data_library)
print("--- 1. Original Data ---")
print(df_library.head())

X=df_library.drop( columns='Return_Status')
y=df_library['Return_Status']
print(X)
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.25, random_state=42, stratify=y

)

encoder=OneHotEncoder(drop='first',sparse_output=False)

train_encoded=encoder.fit_transform(X_train[['Department','Book_Category']])
test_encoded=encoder.transform(X_test[['Department','Book_Category']])

features=encoder.get_feature_names_out(['Department','Book_Category'])

df_tem_train=pd.DataFrame(train_encoded,columns=features,index=X_train.index)
df_tem_test=pd.DataFrame(test_encoded,columns=features,index=X_test.index)

df_final_train=pd.concat([X_train[['Student_ID']],df_tem_train],axis=1)
df_final_test=pd.concat([X_test[['Student_ID']],df_tem_test],axis=1)
print(df_tem_test)
print(df_tem_train)

