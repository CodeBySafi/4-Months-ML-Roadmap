import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data_server = {
    'Response_Time_ms': [12, 15, 20, 18, -5, 22, 25, 30, 8000, 28, 35, 40, 45, 50, 48, 55, 60, 65, 70, 75],
    'Traffic_Status': ['Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'High', 'Low', 
                       'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High']
}
df_server = pd.DataFrame(data_server)
print("--- Original Data ---")
print(df_server.head())



X=df_server[['Response_Time_ms']]
y=df_server[ 'Traffic_Status']

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.25, random_state=42, stratify=y 

)

upper=X_train['Response_Time_ms'].quantile(0.95)
lower=X_train['Response_Time_ms'].quantile(0.05)

trim_X_train=X_train.loc[(X_train['Response_Time_ms']>=lower)&(X_train['Response_Time_ms']<=upper)]
trim_X_test=X_test.loc[(X_test['Response_Time_ms']>=lower)&(X_test['Response_Time_ms']<=upper)]


print(trim_X_test)
print(trim_X_train)


cap_X_train=np.where(X_train['Response_Time_ms']>upper,upper,np.where(X_train['Response_Time_ms']<lower,lower,X_train['Response_Time_ms']))
cap_X_test=np.where(X_test['Response_Time_ms']>upper,upper,np.where(X_test['Response_Time_ms']<lower,lower,X_test['Response_Time_ms']))



print("\n--- Capped X_train (Dekhein -5 aur 8000 theek hue?) ---")
print(cap_X_train)

print("\n--- Capped X_test ---")
print(cap_X_test)