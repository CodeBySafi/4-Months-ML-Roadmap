import pandas as pd
from sklearn.preprocessing import StandardScaler


customer_data = {
    'Customer_ID': [101, 102, 103, 104, 105],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi'],
    'Age': [25, None, 35, 45, None]
}
df_customers = pd.DataFrame(customer_data)

purchase_data = {
    'Customer_ID': [101, 103, 104, 105, 106], 
    'Total_Spend': [5000, 12000, 45000, 20000, 8000]
}
df_purchases = pd.DataFrame(purchase_data)

df_merge=pd.merge(df_customers,df_purchases,on="Customer_ID",how="inner")
print(df_merge)

men=df_merge['Age'].mean()

df_merge["Age"]=df_merge['Age'].fillna(men)
print(df_merge)

df_encoded=pd.get_dummies(df_merge,columns=["City"],dtype=int)
print(df_encoded)
scaler=StandardScaler()

df_encoded[["Age","Total_Spend"]]=scaler.fit_transform(df_encoded[["Age","Total_Spend"]])
print(df_encoded)