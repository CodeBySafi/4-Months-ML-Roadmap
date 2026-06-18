import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    'Emp_ID': [1, 2, 3, 4, 5],
    'Age': [22, 28, 35, 42, 50],
    'Salary': [35000, 48000, 75000, 110000, 150000]
}
df = pd.DataFrame(data)

print("Original Data:\n", df)
print("\n--------------------------\n")

minmax=MinMaxScaler()
df_minmax=pd.DataFrame(minmax.fit_transform(df),columns=df.columns)
print(df_minmax)

scaler=StandardScaler()
std_scaler=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(std_scaler)