import pandas as pd 
student_data = {
    "Roll_No": [101, 102, 103, 104, 105],
    "Name": ["Ali", "Sara", "Ahmad", "Fatima", "Usman"],
    "Degree": ["SE", "CS", "SE", "IT", "SE"],
    "CGPA": [3.5, 3.8, 2.9, 3.6, 3.2]
}
data=pd.DataFrame(student_data)

print(data)

print(data.head(3))

print(data.info())

print(data.shape)

print(data.columns)