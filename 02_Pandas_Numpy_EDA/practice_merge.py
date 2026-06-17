import pandas as pd

# Table 1: Students ki detail
students_data = {
    'Roll_No': [101, 102, 103],
    'Name': ['Ali', 'Ayesha', 'Bilal']
}
df_students = pd.DataFrame(students_data)

# Table 2: Database Exam ke Marks
marks_data = {
    'Roll_No': [101, 103, 104],
    'DB_Marks': [85, 90, 75]
}
df_marks = pd.DataFrame(marks_data)

print("Students Table:")
print(df_students)
print("\nMarks Table:")
print(df_marks)
print("\n--- Final Result Niche Hai ---\n")

final_result =pd.merge(df_students,df_marks,on='Roll_No',how='inner')
print(final_result)