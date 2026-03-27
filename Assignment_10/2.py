# ==============================
# Q2: Employee Excel Program
# ==============================

import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

print("Employee Data:\n", df)


# a) Print list of employees in "Automotive" domain

print("\nEmployees in Automotive Domain:")
auto_emp = df[df["Domain"] == "Automotive"]
print(auto_emp)


# b) Print details using Employee ID (user input)

emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df["Employee ID"] == emp_id]

print("\nEmployee Details:")
print(emp_details)


# c) Print list of Developers

print("\nList of Developers:")
developers = df[df["Designation"] == "Developer"]
print(developers)