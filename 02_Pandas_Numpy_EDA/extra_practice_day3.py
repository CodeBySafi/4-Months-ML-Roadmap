import pandas as pd

store_data = {
    "Product_ID": [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512],
    "Item_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Router", "GPU", "RAM", "SSD"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Networking", "Electronics", "Electronics", "Electronics"],
    "Price_PKR": [150000, 2500, 4500, 35000, 85000, 6000, 15000, 45000, 8000, 110000, 12000, 18000],
    "Stock": [3, 15, 20, 4, 8, 0, 12, 2, 6, 1, 25, 0],
    "Rating": [4.5, 4.2, 4.0, 4.6, 4.7, 3.9, 4.1, 4.3, 3.8, 4.8, 4.4, 4.5]
}

df = pd.DataFrame(store_data)
print(df)


print(df[["Item_Name","Price_PKR","Rating"]])
print(df.iloc[1:10:2,[1,3]])
lists=df.loc[((df[ "Category"]=="Electronics")|(df["Price_PKR"]>10000))&(df["Stock"]<5)]
print(lists)