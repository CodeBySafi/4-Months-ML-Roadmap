import pandas as pd
import numpy as np

bank_data = {
    "Account_No": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman", "Ayesha", "Bilal"],
    "Account_Type": ["Current", "Saving", "Current", "Saving", "Current", "Saving", "Saving"],
    "Initial_Balance": [50000, 120000, 30000, 80000, 45000, 150000, 20000],
    "Deposits": [15000, np.nan, 20000, 5000, np.nan, 25000, 8000],
    "Withdrawals": [5000, 10000, np.nan, np.nan, 15000, 20000, 2000]
}

df = pd.DataFrame(bank_data)

df["Deposits"]=df["Deposits"].fillna(0)
df["Withdrawals"]=df["Withdrawals"].fillna(0)


df["Final_Balance"]=df["Initial_Balance"]+df["Deposits"]-df["Withdrawals"]
print(df)

final=df.loc[df["Final_Balance"]>80000].sort_values("Final_Balance",ascending=False)
print(final)

accounts=df.groupby(by= "Account_Type")["Final_Balance"].mean()
print(accounts)