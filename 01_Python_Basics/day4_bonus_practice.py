import pandas as pd
import numpy as np

exam_data = {
    "Student_ID": ["ARID-01", "ARID-02", "ARID-03", "ARID-04", "ARID-05", "ARID-06", "ARID-07", "ARID-08"],
    "Name": ["Safiullah", "Ahmad", "Sara", "Fatima", "Usman", "Bilal", "Ayesha", "Omer"],
    "Subject": ["DBMS", "DLD", "DBMS", "OOP", "DLD", "OOP", "DBMS", "DLD"],
    "Mid_Term": [28, 22, np.nan, 25, 18, np.nan, 27, 20],
    "Final_Term": [45, 40, 38, np.nan, 35, 48, 42, np.nan]
}

df = pd.DataFrame(exam_data)

df[ "Mid_Term"]=df[ "Mid_Term"].fillna(0)
df[ "Final_Term"]=df[ "Final_Term"].fillna(0)
print(df)
df["Grand_total"]=df[ "Mid_Term"]+df[ "Final_Term"]
print(df)
topper=df.loc[(df["Grand_total"]>60)].sort_values(by=["Grand_total"],ascending=False)
print(topper)

book_score=df.groupby("Subject")["Grand_total"].max()
print(book_score)