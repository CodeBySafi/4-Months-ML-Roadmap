import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

applicant_data = {
    'App_ID': [1001, 1002, 1003, 1004, 1005, 1006],
    'Age': [25, 32, None, 45, 29, 50],
    'Income': [50000, 120000, 80000, None, 45000, 200000],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Lahore', 'Karachi', 'Islamabad']
}

credit_data = {
    'App_ID': [1001, 1002, 1003, 1004, 1005], 
    'Credit_Score': [600, 750, 680, 800, 550],
    'Existing_Loan': [0, 15000, 0, 50000, 10000]
}


df_ap=pd.DataFrame(applicant_data)
df_cr=pd.DataFrame(credit_data)


df_bank=pd.merge(df_ap,df_cr,on= 'App_ID',how='inner') 
print(df_bank)

med=df_bank["Age"].median()
df_bank["Age"]=df_bank["Age"].fillna(med)
men=df_bank["Income"].mean()
df_bank["Income"]=df_bank["Income"].fillna(men)
print(df_bank)


df_bank["net_Income"]=df_bank['Income']-df_bank['Existing_Loan']
print(df_bank)


df_premium=df_bank.loc[(df_bank['Credit_Score']>650)&(df_bank["net_Income"]>50000)]
print(df_premium)

group_data=df_bank.groupby("City")['Credit_Score'].mean()
print(group_data)

scaler=StandardScaler()

df_bank[["Income" ,"Credit_Score"]]=scaler.fit_transform(df_bank[["Income" ,"Credit_Score"]])
print(df_bank)