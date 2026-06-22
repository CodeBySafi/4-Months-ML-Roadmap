import pandas as pd
from sklearn.model_selection import train_test_split

data_med = {
    'Patient_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Blood_Pressure': [120, 140, 115, 150, 118, 135, 122, 145],
    'Cholesterol': [180, 240, 170, 260, 190, 220, 185, 250],
    'Doctor_Name': ['Dr. Ali', 'Dr. Sara', 'Dr. Ali', 'Dr. Sara', 'Dr. Ali', 'Dr. Sara', 'Dr. Ali', 'Dr. Sara'],
    'Disease_Status': ['Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Negative', 'Negative', 'Positive']
}
df_med = pd.DataFrame(data_med)
print("\n--- Medical Data ---")
print(df_med)


X = df_med.drop(['Patient_ID', 'Doctor_Name', 'Disease_Status'], axis=1)
y=df_med['Disease_Status']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,test_size=0.25,random_state=42,stratify=y

)

print(y_train.value_counts(normalize=True)*100)
print(y_test.value_counts(normalize=True)*100)


