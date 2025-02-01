from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    try:
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute(query, args)
        result = cursor.fetchall()
        conn.close()
        return (result[0] if result else None) if one else result
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").lower()

    if "employees in" in user_input:
        department = user_input.split("in ")[-1].strip().title()
        employees = query_db("SELECT Name FROM Employees WHERE Department = ?", (department,))
        if employees:
            response = f"Employees in {department} Department are:\n"
            response += "\n".join([e[0] for e in employees])
        else:
            response = "No employees found."

    elif "manager of" in user_input:
        department = user_input.split("of ")[-1].strip().title()
        manager = query_db("SELECT Manager FROM Departments WHERE Name = ?", (department,), one=True)
        response = f"The manager of {department} is {manager[0]}." if manager else "Department not found."

    elif "hired after" in user_input:
        date = user_input.split("after ")[-1].strip()
        employees = query_db("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        if employees:
            response = f"Employees hired after {date} are:\n"
            response += "\n".join([e[0] for e in employees])
        else:
            response = f"No employees found hired after {date}."

    elif "total salary expense for" in user_input:
        department = user_input.split("for ")[-1].strip().title()
        total_salary = query_db("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,), one=True)
        response = f"Total salary expense for {department}: {total_salary[0] if total_salary and total_salary[0] else 0}"

    elif "employee count in" in user_input:
        department = user_input.split("in ")[-1].strip().title()
        count = query_db("SELECT COUNT(*) FROM Employees WHERE Department = ?", (department,), one=True)
        if count:
            response = f"There are {count[0]} employees in the {department} department."
        else:
            response = f"No employees found in the {department} department."

    else:
        response = "I don't understand that query."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
