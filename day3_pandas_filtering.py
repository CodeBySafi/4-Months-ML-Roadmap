import pandas as pd
tech_data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman", "Ayesha", "Bilal", "Zainab", "Omer", "Khadija"],
    "City": ["Sahiwal", "Lahore", "Islamabad", "Sahiwal", "Karachi", "Lahore", "Sahiwal", "Islamabad", "Multan", "Sahiwal"],
    "Role": ["Data Scientist", "Web Dev", "Data Scientist", "App Dev", "ML Engineer", "Web Dev", "App Dev", "ML Engineer", "DevOps", "Data Scientist"],
    "CGPA": [3.2, 3.8, 3.5, 2.9, 3.9, 3.1, 3.6, 3.7, 2.8, 3.4],
    "Salary_PKR": [120000, 85000, 140000, 75000, 180000, 90000, 80000, 160000, 110000, 130000],
    "Experience_Yrs": [1, 3, 2, 0, 4, 1, 2, 3, 1, 2]
}

df=pd.DataFrame(tech_data)
print(df[["Name","Role","Salary_PKR"]])
print(df.iloc[3:8,0:3])
fitered_data=df.loc[(df["City"]=="Sahiwal")&(df["Role"]=="Data Scientist")&(df["CGPA"]>3.0)]
print(fitered_data)