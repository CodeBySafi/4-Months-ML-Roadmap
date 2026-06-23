import pandas as pd
import numpy as np

data_heights = {
    'Student_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12'],
    'Height_cm': [165, 170, 180, 168, 350, 172, 175, 160, 20, 182, 178, 169]
}
df_heights = pd.DataFrame(data_heights)
print("--- Heights Data ---")
print(df_heights)


Q1=df_heights['Height_cm'].quantile(0.25)
Q3=df_heights['Height_cm'].quantile(0.75)

IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

outlier=df_heights.loc[(df_heights['Height_cm']<lower_bound)|(df_heights['Height_cm']>upper_bound)]
clean=df_heights.loc[(df_heights['Height_cm']>=lower_bound)&(df_heights['Height_cm']<=upper_bound)]

print(outlier)
print(clean)