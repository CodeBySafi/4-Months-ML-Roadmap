
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

hr_data = {
    'Emp_ID': [101, 102, 103, 104, 105, 106],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'Marketing'],
    'Age': [28, 35, None, 42, 25, None],
    'Years_Experience': [5, 10, 3, 15, 2, 8]
}

finance_data = {
    'Emp_ID': [101, 102, 103, 104, 105], # Emp_ID 106 ka data missing hai
    'Base_Salary': [60000, 85000, 50000, 120000, 45000],
    'Performance_Rating': [4.5, 3.8, 4.0, 4.8, 3.5]

}

hr_da=pd.DataFrame(hr_data)
print(hr_da)

fin_data=pd.DataFrame(finance_data)
print(fin_data)

df_startup=pd.merge(hr_da,fin_data,on="Emp_ID",how="inner")
print(df_startup)

men=df_startup["Age"].mean()
df_startup["Age"]=df_startup["Age"].fillna(men)
print(df_startup)

bonus = np.array([10000])
df_startup["Total_Salary"]=df_startup[ 'Base_Salary']+bonus
print(df_startup)


df_stars=df_startup.loc[(df_startup["Performance_Rating"]>=4.0)&(df_startup["Total_Salary"]<65000)]
print(df_stars)

average_salary=df_startup.groupby("Department")["Total_Salary"].mean()
print(average_salary)

df_startup=pd.get_dummies(df_startup,columns=["Department"],dtype=int)
print(df_startup)
 
arr1=np.array(df_startup["Years_Experience"])
exp_matri=arr1.reshape(-1,1)
print(exp_matri)


scaler=MinMaxScaler()
df_startup[['Total_Salary']]=scaler.fit_transform(df_startup[['Total_Salary']])
print(df_startup)