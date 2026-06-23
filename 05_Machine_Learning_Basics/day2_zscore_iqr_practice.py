from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

data_scores = {
    'Roll_No': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Marks': [65, 70, 68, 72, -20, 75, 69, 150, 71, 66]
}
df_scores = pd.DataFrame(data_scores)
print("--- Exam Scores Data ---")
print(df_scores)

standrd =StandardScaler()

df_scores["Z_score"]=standrd.fit_transform(df_scores[[ 'Marks']])
print(df_scores)

outlier=df_scores.loc[np.abs(df_scores[ 'Z_score'])>3]

clean_z=df_scores.loc[np.abs(df_scores[ 'Z_score'])<=3]
print(clean_z)
print(outlier)





data_temp = {
    'Day': ['June 1', 'June 2', 'June 3', 'June 4', 'June 5', 'June 6', 'June 7', 'June 8', 'June 9'],
    'Temperature_C': [42, 45, 41, 180, 44, 43, 40, 0, 46]
}
df_temp = pd.DataFrame(data_temp)
print("\n--- Temperature Data ---")
print(df_temp)


Q1=df_temp['Temperature_C'].quantile(0.25)
Q3=df_temp['Temperature_C'].quantile(0.75)
IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

outlier=df_temp.loc[(df_temp['Temperature_C']<lower_bound)|(df_temp['Temperature_C']>upper_bound)]
clean=df_temp.loc[(df_temp['Temperature_C']>=lower_bound)&(df_temp['Temperature_C']<=upper_bound)]
print("Outlier are \n",outlier)
print("Clean data is\n",clean)


