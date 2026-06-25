import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

data_customers = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Membership_Level': ['Bronze', 'Gold', 'Silver', 'Bronze', 'Platinum', 'Silver', 'Gold', 'Bronze', 'Platinum', 'Silver'],
    'Bought_Premium_Item': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes'] # Target
}
df_customers = pd.DataFrame(data_customers)
print("--- Original Data ---")
print(df_customers)



X=df_customers[ ['Membership_Level']]
y=df_customers[ 'Bought_Premium_Item']

X_train,X_test,y_train,y_test=train_test_split(

    X,
    y,test_size=0.2, random_state=42,stratify=y

)

level=["Bronze", "Silver", "Gold", "Platinum"]
encoded=OrdinalEncoder(categories=[level])

X_train["Encoded X_train"]=encoded.fit_transform(X_train[['Membership_Level']])
X_test["Encoded X_train"]=encoded.transform(X_test[['Membership_Level']])

print(X_train)
print(X_test)