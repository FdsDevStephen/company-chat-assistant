import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Query 1: Show all employees in a specific department
department = "Sales"
cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (department,))
employees = cursor.fetchall()
print(f"Employees in {department} department: {employees}")

# Query 2: Who is the manager of a department?
department = "Engineering"
cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
manager = cursor.fetchone()
print(f"Manager of {department} department: {manager[0] if manager else 'Not found'}")

# Query 3: List all employees hired after a certain date
hire_date = "2021-01-01"
cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (hire_date,))
new_employees = cursor.fetchall()
print(f"Employees hired after {hire_date}: {new_employees}")

# Query 4: Total salary expense for a department
department = "Marketing"
cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
total_salary = cursor.fetchone()
print(f"Total salary expense for {department} department: {total_salary[0] if total_salary[0] else 0}")

conn.close()
