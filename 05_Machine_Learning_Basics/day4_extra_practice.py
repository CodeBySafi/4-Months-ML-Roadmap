import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

# --- Dummy Data: Component Quality ---
data_components = {
    'Component_ID': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
    'Component_Type': ['AND_Gate', 'D_Latch', 'OR_Gate', 'Mux', 'AND_Gate', 'D_Latch', 'Encoder', 'Decoder', 'OR_Gate', 'Mux'],
    'Tolerance_Grade': ['Consumer', 'Military', 'Industrial', 'Consumer', 'Automotive', 'Industrial', 'Military', 'Consumer', 'Automotive', 'Industrial'],
    'Pass_Stress_Test': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes'] # Target
}
df_components = pd.DataFrame(data_components)
print("--- Original Data ---")
print(df_components)


X=df_components[['Tolerance_Grade']]
y=df_components[ 'Pass_Stress_Test']
X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.3, random_state=42, stratify=y
)

level=['Consumer','Industrial', 'Automotive', 'Military']
encoder=OrdinalEncoder(categories=[level])
X_train["Encoded_value"]=encoder.fit_transform(X_train[['Tolerance_Grade']])
X_test["Encoded_value"]=encoder.transform(X_test[['Tolerance_Grade']])
print(X_train)
print(X_test)