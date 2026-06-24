import pandas as pd
from sklearn.model_selection import train_test_split

data_delivery = {
    'Delivery_Minutes': [25, 30, 22, 45, -10, 35, 40, 28, 500, 32, 20, 27, 42, 38, 600, 24, 29, 31, 26, -5],
    'Review': ['Good', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad', 'Good', 'Bad', 'Good', 
               'Good', 'Good', 'Bad', 'Bad', 'Bad', 'Good', 'Good', 'Good', 'Good', 'Good']
}
df_delivery = pd.DataFrame(data_delivery)
print("--- Original Data ---")
print(df_delivery.head())



X=df_delivery[['Delivery_Minutes']]
y=df_delivery ['Review']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25, random_state=42, stratify=y

)

lower=X_train['Delivery_Minutes'].quantile(0.05)
upper=X_train['Delivery_Minutes'].quantile(0.95)

condition=(X_train['Delivery_Minutes']>=lower)&(X_train['Delivery_Minutes']<=upper)
X_train_trim=X_train.loc[condition]
y_train_trim=y_train.loc[condition]

condition_test=(X_test['Delivery_Minutes']>=lower)&(X_test['Delivery_Minutes']<=upper)

X_test_trim=X_test.loc[condition_test]
y_test_trim=y_test.loc[condition_test]

print("X_train_trim",len(X_train_trim))
print("y_train_trim",len(y_train_trim))
print("X_test_trim",len(X_test_trim))
print("y_test_trim",len(y_test_trim))

