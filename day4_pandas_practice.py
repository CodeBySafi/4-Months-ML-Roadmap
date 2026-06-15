import pandas as pd
import numpy as np

freelance_data = {
    "Profile_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman", "Ayesha", "Bilal", "Zainab", "Omer", "Khadija", "Hassan", "Maryam"],
    "Skill": ["Python", "SEO", "Python", "Graphic Design", "SEO", "Python", "Graphic Design", "SEO", "Python", "Graphic Design", "SEO", "Python"],
    "Earnings_USD": [1200, 800, np.nan, 450, 900, 1500, np.nan, 1100, 1300, 500, np.nan, 1600],
    "Rating": [4.8, 4.5, 4.9, np.nan, 4.7, 4.9, 4.2, 4.8, np.nan, 4.6, 4.3, 5.0]
}

df = pd.DataFrame(freelance_data)

df["Rating"]=df["Rating"].fillna(0.0)
df["Earnings_USD"]=df["Earnings_USD"].fillna(0)
df=df.drop("Profile_ID",axis=1)
print(df)
df["Earnings_PKR"]=df["Earnings_USD"]*280
high_pay=df.sort_values(by="Earnings_PKR",ascending=False)
print(high_pay)
total_eraning=df.groupby( "Skill")["Earnings_USD"].sum()
print(total_eraning)