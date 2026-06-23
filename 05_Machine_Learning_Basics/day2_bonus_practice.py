import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# --- Task 1 Data: House Prices (in Lakhs) ---
data_houses = {
    'House_ID': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'],
    'Bedrooms': [2, 3, 2, 4, 3, 2, 6, 3, 2, 3],
    'Price_Lakhs': [45, 50, 42, 60, 900, 48, 55, -10, 47, 52] 
    # Outliers: 900 aur -10
}
df_houses = pd.DataFrame(data_houses)
print("--- Real Estate Data ---")
print(df_houses)

# 👇 TASK 1: Yahan IQR method use kar ke 'Price_Lakhs' column ke outliers nikalen aur clean data print karein.

q1=df_houses["Price_Lakhs"].quantile(0.25)
q3=df_houses["Price_Lakhs"].quantile(0.75)

IQR=q3-q1

lower=q1-1.5*IQR
upper=q3+1.5*IQR


outlier=df_houses.loc[(df_houses['Price_Lakhs']<lower)|(df_houses['Price_Lakhs']>upper)]

clear=df_houses.loc[(df_houses['Price_Lakhs']>=lower)&(df_houses['Price_Lakhs']<=upper)]

print(outlier)
print(clear)




# --- Task 2 Data: Heart Rate (BPM) ---
data_hr = {
    'Time_Seconds': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Heart_Rate_BPM': [72, 75, 71, 74, 250, 73, 76, 0, 72, 70]
    # Outliers: 250 aur 0
}
df_hr = pd.DataFrame(data_hr)
print("\n--- Heart Rate Data ---")
print(df_hr)

# 👇 TASK 2: Yahan StandardScaler use kar ke Z-Score method se 'Heart_Rate_BPM' ke outliers nikalen aur clean data print karein.


scaler=StandardScaler()
df_hr["Z_score"]=scaler.fit_transform(df_hr[['Heart_Rate_BPM']])
print(df_hr)


outlr=df_hr.loc[np.abs(df_hr["Z_score"])>3]
clr=df_hr.loc[np.abs(df_hr["Z_score"])<=3]
print(outlr)
print(clr)