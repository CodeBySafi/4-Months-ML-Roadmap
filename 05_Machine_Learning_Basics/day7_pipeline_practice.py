import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

data_students = {
    'Student_ID': ['Arid-01', 'Arid-02', 'Arid-03', 'Arid-04', 'Arid-05', 'Arid-06'],
    'Study_Hours': [4, 6, np.nan, 2, 7, np.nan],         
    'Attendance': [85, np.nan, 70, 50, 95, 60],           
    'Favorite_Subject': ['OOP', 'DLD', 'DBMS', np.nan, 'OOP', 'DBMS'],
    'Passed': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']   
}
df = pd.DataFrame(data_students)
print("--- 1. Original Dirty Data ---")
print(df)




X=df[['Study_Hours', 'Attendance','Favorite_Subject']]
y=df['Passed']

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.3, random_state=42, stratify=y
)

num_pipe=Pipeline(steps=[
    ("step_1",SimpleImputer(strategy="mean")),
    ("step_2",StandardScaler())
])

text_pipe=Pipeline(steps=[
    ("step_1",SimpleImputer(strategy="most_frequent")),
    ("step_2",OneHotEncoder(drop='first', sparse_output=False))
])

manager=ColumnTransformer(transformers=[
    ("num",num_pipe,['Study_Hours', 'Attendance'])
    ,('text',text_pipe,["Favorite_Subject"])
])

clean_train=manager.fit_transform(X_train)
clean_test=manager.transform(X_test)

print(clean_train)
print(clean_test)

df_train=pd.DataFrame(clean_train)
df_test=pd.DataFrame(clean_test)

print(df_train)
print(df_test)