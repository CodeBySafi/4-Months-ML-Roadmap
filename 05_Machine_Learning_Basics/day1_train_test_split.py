import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Hours_Studied': [5, 2, 7, 3, 8, 1, 6, 4, 9, 2, 5, 8],
    'Attendance_Percentage': [80, 50, 90, 60, 95, 40, 85, 70, 98, 55, 75, 92],
    'Result': ['Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']
}

df = pd.DataFrame(data)



X=df[[ 'Hours_Studied','Attendance_Percentage']]
y=df["Result"]

X_train,X_test,y_train,y_test=train_test_split(

X,y,test_size=0.25,random_state=42,stratify=y
)

print(y_train.value_counts(normalize=True)*100)
print(y_test.value_counts(normalize=True)*100)
