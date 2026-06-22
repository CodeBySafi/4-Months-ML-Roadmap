import pandas as pd
from sklearn.model_selection import train_test_split

data_ecom = {
    'Transaction_ID': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'],
    'Customer_Rating': [5, 1, 4, 2, 5, 3, 4, 5, 1, 5],
    'Delivery_Days': [2, 8, 3, 7, 1, 4, 2, 1, 6, 2],
    'Product_Price': [1500, 2500, 800, 3000, 1200, 500, 900, 4000, 2200, 1000],
    'Returned': ['No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No']
}
df_ecom = pd.DataFrame(data_ecom)
print("--- E-commerce Data ---")
print(df_ecom)



X=df_ecom.drop(['Returned','Transaction_ID'],axis=1)
y=df_ecom["Returned"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,random_state=101,test_size=0.2,stratify=y
)
print(y_train.value_counts(normalize=True)*100)
print(y_test.value_counts(normalize=True)*100)