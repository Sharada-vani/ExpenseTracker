from openpyxl import Workbook
import sqlite3

def login():
    print("----- LOGIN -----")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful\n")
        return True
    else:
        print("Invalid Credentials\n")
        return False

# Create Database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()
conn.close()


# Add Expense
def add_expense():
    category = input("Enter Category: ").strip()

    if category == "":
        print("Category cannot be empty")
        return

    try:
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0")
            return

    except:
        print("Invalid amount")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    if date == "":
        print("Date cannot be empty")
        return

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(category, amount, date) VALUES (?, ?, ?)",
        (category, amount, date)
    )

    conn.commit()
    conn.close()

    print("Expense Added Successfully")



# View Expenses
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No expenses found")

    else:
        for row in records:
            print(row)

    conn.close()


# Delete Expense
def delete_expense():
    try:
        expense_id = int(input("Enter Expense ID to Delete: "))
    except:
        print("Invalid ID")
        return

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    if cursor.rowcount == 0:
        print("No record found")
    else:
        print("Expense Deleted")

    conn.commit()
    conn.close()

def update_expense():
    try:
        expense_id = int(input("Enter Expense ID: "))
    except:
        print("Invalid ID")
        return

    category = input("New Category: ").strip()

    try:
        amount = float(input("New Amount: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            return
    except:
        print("Invalid amount")
        return

    date = input("New Date (YYYY-MM-DD): ").strip()

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE expenses
    SET category = ?, amount = ?, date = ?
    WHERE id = ?
    """, (category, amount, date, expense_id))

    if cursor.rowcount == 0:
        print("No record found")
    else:
        print("Expense Updated Successfully")

    conn.commit()
    conn.close()

# Total Expense
def total_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    print("Total Expense:", total)

    conn.close()

def category_summary():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    records = cursor.fetchall()

    print("\nCategory Wise Summary")

    for row in records:
        print(row[0], ":", row[1])

    conn.close()

def monthly_summary():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT substr(date, 1, 7) as month, SUM(amount)
    FROM expenses
    GROUP BY month
    ORDER BY month
    """)

    records = cursor.fetchall()

    print("\nMonthly Expense Summary")

    for row in records:
        print(row[0], ":", row[1])

    conn.close()

def search_by_date():

    date = input("Enter Date (YYYY-MM-DD): ")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE date = ?",
        (date,)
    )

    records = cursor.fetchall()

    if len(records) == 0:
        print("No expenses found for this date")

    else:
        for row in records:
            print(row)

    conn.close()

def export_to_excel():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    wb = Workbook()
    ws = wb.active

    ws.title = "Expenses Report"

    # Header row
    ws.append(["ID", "Category", "Amount", "Date"])

    # Data rows
    for row in records:
        ws.append(row)

    wb.save("expenses_report.xlsx")

    conn.close()

    print("Excel file created: expenses_report.xlsx")

# Main Menu

if not login():
    exit()

while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2.View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Total Expense")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Search by Date")
    print("9. Export to Excel")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
       update_expense()

    elif choice == "5":
        total_expense()

    elif choice == "6":
        category_summary()

    elif choice == "7":
        monthly_summary()

    elif choice == "8":
       search_by_date()

    elif choice == "9":
       export_to_excel()

    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")