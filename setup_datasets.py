import pandas as pd
import numpy as np

# retail_sales.csv
# OrderID, CustomerID, ProductCategory, SalesAmount, Region, and OrderDate. 
data_retail = {
    'OrderID': range(1, 21),
    'CustomerID': np.random.randint(100, 200, 20),
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Home', 'Electronics', 'Clothing', 'Electronics', 'Electronics', 'Home']*2,
    'SalesAmount': [200, 50, np.nan, 300, 40, np.nan, 60, np.nan, 400, 50, 210, 55, np.nan, np.nan, 45, 230, 65, 350, np.nan, 55],
    'Region': ['North', 'South', 'South', 'East', 'West', 'South', 'North', 'West', 'South', 'East']*2,
    'OrderDate': pd.date_range('2023-01-01', periods=20)
}
df_retail = pd.DataFrame(data_retail)
df_retail.to_csv('retail_sales.csv', index=False)

# employee_master.csv
# Employee_Name
data_employee = {
    'EmployeeID': range(1, 11),
    'Employee_Name': [
        'Dr. Rahul Kumar Sharma',
        'Priya M.',
        'Mr. S. Venkatesh',
        'Ms. Priya M.',
        'Rahul Sharma',
        'Rahul K. Sharma',
        'Dr. Amit Singh',
        'Amit Singh',
        'S. Venkatesh',
        'Mr. John Doe'
    ]
}
df_employee = pd.DataFrame(data_employee)
df_employee.to_csv('employee_master.csv', index=False)

# student_personal.csv (StudentID, Name, Department, Year)
data_student = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['CSE', 'ECE', 'CSE', 'MECH', 'ECE'],
    'Year': [2, 3, 2, 4, 3]
}
df_student = pd.DataFrame(data_student)
df_student.to_csv('student_personal.csv', index=False)

# exam_scores.csv (StudentID, Subject, Marks, ExamType)
data_exam = {
    'StudentID': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'Subject': ['Math', 'Physics', 'Math', 'Physics', 'Math', 'Physics', 'Math', 'Physics', 'Math', 'Physics'],
    'Marks': [85, 90, 78, 88, 92, 85, 60, 70, 88, 84],
    'ExamType': ['Midterm', 'Midterm', 'Midterm', 'Midterm', 'Final', 'Final', 'Final', 'Final', 'Midterm', 'Midterm']
}
df_exam = pd.DataFrame(data_exam)
df_exam.to_csv('exam_scores.csv', index=False)

print("Datasets created successfully.")
