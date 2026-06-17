import pandas as pd

details = {
    "Roll_No": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman"],
    "Degree": ["SE", "CS", "SE", "IT", "SE"],
    "CGPA": [3.1, 3.8, 2.9, 3.6, 3.9],
    "City": ["Sahiwal", "Lahore", "Sahiwal", "Multan", "Sahiwal"]
}

data=pd.DataFrame(details)
# print(data)

# print(data["Name"])
# print(data[["Name","CGPA","City"]])

# print(data.iloc[1:3,0:2])

filter=data.loc[(data["City"]=="Sahiwal") & (data["CGPA"]>3.5) ]
print(filter)