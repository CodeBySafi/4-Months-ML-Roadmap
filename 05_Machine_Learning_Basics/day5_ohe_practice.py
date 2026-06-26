import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

data_factory = {
    'Batch_ID': ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08'],
    'Plant': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Islamabad', 'Lahore', 'Karachi'],
    'Gate_Type': ['OR_Gate', 'AND_Gate', 'MUX', 'OR_Gate', 'D_Latch', 'AND_Gate', 'MUX', 'D_Latch'], 
    'Defective': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes'] 
}
df_factory = pd.DataFrame(data_factory)
print("--- 1. Original Data ---")
print(df_factory.head())



X=df_factory[['Plant','Gate_Type']]
y=df_factory['Defective']

X_train,X_test,y_train,y_test=train_test_split(

    X,y,test_size=0.25, random_state=42, stratify=y
)

encoder=OneHotEncoder(drop='first',sparse_output=False)

X_train_Ohe=encoder.fit_transform(X_train[['Plant','Gate_Type']])

X_test_Ohe=encoder.transform(X_test[['Plant','Gate_Type']])

feature=encoder.get_feature_names_out(['Plant','Gate_Type'])

df_encoded_train=pd.DataFrame(X_train_Ohe,columns=feature,index=X_train.index)
df_encoded_test=pd.DataFrame(X_test_Ohe,columns=feature,index=X_test.index)

print(df_encoded_test)
print(df_encoded_train)
