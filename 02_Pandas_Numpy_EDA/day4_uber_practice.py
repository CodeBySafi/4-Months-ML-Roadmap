import pandas as pd
import numpy as np

ride_data = {
    "Ride_ID": ["R-01", "R-02", "R-03", "R-04", "R-05", "R-06", "R-07", "R-08"],
    "Driver_Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman", "Bilal", "Ayesha", "Omer"],
    "Car_Type": ["Mini", "Go", "Mini", "Go+", "Go", "Mini", "Go+", "Go"],
    "Distance_km": [12.5, 8.0, np.nan, 25.0, 5.5, np.nan, 15.0, 10.2],
    "Fare_PKR": [850, 600, np.nan, 1800, 450, 300, 1200, np.nan],
    "Rating": [4.5, np.nan, 4.8, 4.9, 4.2, 4.1, 5.0, 4.6]
}

df = pd.DataFrame(ride_data)
df=df.dropna()
print(df)

df["Rate_Per_Km"]=df["Fare_PKR"]/df["Distance_km"]
print(df)

top_tire=df.loc[(df["Car_Type"]=="Go+")&(df[ "Rating"]>4.5)].sort_values("Rate_Per_Km")
print(top_tire)

distance=df.groupby(by="Car_Type")["Distance_km"].sum()
print(distance)
