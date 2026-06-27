import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# --- Dummy Data: Student Records ---
# np.nan ka matlab hai data missing hai
data_students = {
    'Student_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'],
    'Score': [85, 90, np.nan, 75, 88, np.nan], # Numbers (Use Mean)
    'Department': ['SE', np.nan, 'CS', 'SE', 'SE', 'IT'], # Text (Use Most Frequent)
    'Pass': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No'] # Target
}
df_students = pd.DataFrame(data_students)
print("--- 1. Original Data With Missing Values ---")
print(df_students)

# ==========================================
# 👇 YAHAN SE NEECHAY AAPNE CODE LIKHNA HAI 👇
# ==========================================

# Step 1: X aur y banayein ('Student_ID' drop karein)


# Step 2: train_test_split karein (test_size=0.3, random_state=42)
# Target (Pass) categorical hai, isliye stratify=y zaroor lagayein.


# Step 3: Imputers Setup karein
# imputer_num = ... (strategy='mean')
# imputer_cat = ... (strategy='most_frequent')


# Step 4: Golden Rule for 'Score'
# X_train aur X_test ke 'Score' column par imputer_num lagayein
# (Double brackets [[]] use karna mat bhoolna!)


# Step 5: Golden Rule for 'Department'
# X_train aur X_test ke 'Department' column par imputer_cat lagayein


# Final Print: Apna saaf aur theek kiya hua Train data check karein!
# print("\n--- 2. Cleaned X_train ---")
# print(X_train)

# print("\n--- 3. Cleaned X_test ---")
# print(X_test)


X=df_students[[ 'Score','Department']]
y=df_students['Pass']

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.3, random_state=42,stratify=y
)
impute_num=SimpleImputer(strategy='mean')
impute_mf=SimpleImputer(strategy='most_frequent')

X_train["Score"]=impute_num.fit_transform(X_train[['Score']])
X_test["Score"]=impute_num.transform(X_test[['Score']])

X_train['Department']=impute_mf.fit_transform(X_train[['Department']])
X_test['Department']=impute_mf.transform(X_test[['Department']])

print(X_test)
print(X_train)



