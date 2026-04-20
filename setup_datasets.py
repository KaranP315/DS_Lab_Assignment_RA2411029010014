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

print("Datasets created successfully.")
