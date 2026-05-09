import sqlite3

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
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (YYYY-MM-DD): ")

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
    expense_id = int(input("Enter Expense ID to Delete: "))

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()

    print("Expense Deleted")


# Total Expense
def total_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    print("Total Expense:", total)

    conn.close()


# Main Menu
while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_expense()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")