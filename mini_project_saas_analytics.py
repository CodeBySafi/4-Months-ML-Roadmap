import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Raw SaaS Platform Data
saas_data = {
    "Client_ID": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    "Client_Name": ["Alpha Tech", "Beta Corp", "Gamma Studio", "Delta Systems", "Echo Ltd", "Fox Media", "Gulf IT", "Horizon", "Infinity", "Joker Apps"],
    "Product_Category": ["Cloud Storage", "Cybersecurity", "Cloud Storage", "AI Tools", "Cybersecurity", "AI Tools", "Cloud Storage", "AI Tools", "Cybersecurity", "AI Tools"],
    "Monthly_Active_Users": [1200, np.nan, 850, 3100, 450, np.nan, 1500, 2200, 600, 4100],
    "Subscription_Price_USD": [50, 120, 50, 200, 120, 150, 50, 200, np.nan, 250],
    "Server_Cost_USD": [15, 40, 12, 70, 30, 45, 18, np.nan, 20, 90]
}

df = pd.DataFrame(saas_data)
print("--- RAW DATA FROM DATABASE ---")
print(df)

m=df[ "Monthly_Active_Users"].mean()
df[ "Monthly_Active_Users"]=df[ "Monthly_Active_Users"].fillna(m)
df[  "Subscription_Price_USD"]=df[  "Subscription_Price_USD"].fillna(100)
df["Server_Cost_USD"]=df["Server_Cost_USD"].fillna(25)
df=df.drop("Client_ID",axis=1)

print(df)

df["Total_Revenue"]=df["Monthly_Active_Users"]*df["Subscription_Price_USD"]
print(df)

df["Net_Profit"]=df["Total_Revenue"]-df["Server_Cost_USD"]
top_com=df.sort_values("Net_Profit",ascending=False)
print(top_com)

intelligence_sum=df.groupby("Product_Category")["Total_Revenue"].sum()
print(intelligence_sum)
intelligence_mean=df.groupby("Product_Category")["Monthly_Active_Users"].mean()
print(intelligence_mean)


fig,axis=plt.subplots(nrows=1,ncols=2,figsize=(14, 6))

client=df["Client_Name"]

profit=df["Net_Profit"]
user=df["Monthly_Active_Users"]
revenue=df["Total_Revenue"]

axis[0].bar(client,profit,color="skyblue")
axis[0].set_title("Client-wise Net Profit Analysis")
plt.grid(True)

axis[1].scatter(user,revenue,color="darkorange",s=120)
axis[1].set_title("User Growth vs Revenue Correlation")

plt.grid(True)

plt.tight_layout()
plt.show()