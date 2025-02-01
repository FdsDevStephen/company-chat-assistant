import os
import sqlite3

DB_NAME = "company.db"

def database_exists():
    """Check if the database file already exists."""
    return os.path.exists(DB_NAME)

def setup_database():
    """Create tables and insert initial data if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )
    ''')

    # Create Departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
    ''')

    # Insert data only if tables are empty
    cursor.execute("SELECT COUNT(*) FROM Employees")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
        INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)
        ''', [
            ("Alice", "Sales", 50000, "2021-01-15"),
            ("Bob", "Engineering", 70000, "2020-06-10"),
            ("Charlie", "Marketing", 60000, "2022-03-20"),
            ("John Doe", "Sales", 55000, "2022-02-15"),
    ("Jane Smith", "Engineering", 75000, "2019-11-21"),
    ("Mark Taylor", "Marketing", 64000, "2021-06-30"),
    ("Emma Brown", "Sales", 49000, "2020-05-18"),
    ("James Wilson", "Engineering", 80000, "2021-07-23"),
    ("Olivia Harris", "HR", 52000, "2018-03-11"),
    ("Lucas White", "Sales", 57000, "2022-01-28"),
    ("Sophia Lee", "Finance", 65000, "2019-04-10"),
    ("Mason Garcia", "Marketing", 72000, "2020-08-17"),
    ("Ava Martinez", "HR", 54000, "2021-02-05"),
    ("Ethan Davis", "Engineering", 82000, "2020-12-01"),
    ("Chloe Moore", "Sales", 58000, "2021-09-14"),
    ("Benjamin Clark", "Finance", 67000, "2019-10-19"),
    ("Amelia Robinson", "Marketing", 71000, "2021-03-25"),
    ("Alexander Walker", "Engineering", 86000, "2022-04-09")
        ])

        cursor.executemany('''
        INSERT INTO Departments (Name, Manager) VALUES (?, ?)
        ''', [
            ("Sales", "Alice"),
    ("Engineering", "Bob"),
    ("Marketing", "Charlie"),
    ("Sales", "David"),
    ("Engineering", "James"),
    ("HR", "Olivia"),
    ("Sales", "Lucas"),
    ("Finance", "Sophia"),
    ("Marketing", "Mason"),
    ("HR", "Ava"),
    ("Engineering", "Ethan"),
    ("Sales", "Chloe"),
    ("Finance", "Benjamin"),
    ("Marketing", "Amelia"),
    ("Engineering", "Alexander")
        ])

    conn.commit()
    conn.close()
    print("✅ Database is set up and ready.")

if __name__ == "__main__":
    if not database_exists():
        setup_database()
    else:
        print("✅ Database already exists. No changes needed.")
