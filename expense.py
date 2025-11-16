expenses = []


def add_expense():
    item = input("Enter expense item: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"item": item, "amount": amount})
    with open("expenses.txt", "a") as file:
        file.write(f"{item}: ${amount}\n")

    print("Expense added.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['item']}: {expense['amount']}")

def delete_expense():
    view_expenses()
    choice = int(input("Enter the number of the expense to delete: "))
    if choice >= 1 and choice <= len(expenses):        
        removed = expenses.pop(choice - 1)
        with open("expenses.txt", "w") as file:
            for expense in expenses:
                file.write(f"{expense['item']}: ${expense['amount']} \n")
        print(f"Removed expense: {removed['item']}: {removed['amount']}")
    else:
        print("Invalid choice.")

def exit_program():
    print("Program exited.")
    exit()

while True:
    try:
        print("""
    -----Expense Tracker-----
    1. ADD EXPENSE
    2. VIEW EXPENSES
    3. DELETE EXPENSE
    4. EXIT""")
        task = int(input("Choose from 1:4 "))
        if task == 1:
            add_expense()
        elif task == 2:
            view_expenses()
        elif task == 3:
            delete_expense()
        elif task == 4:
            exit_program()
        else:
            print("Invalid choice. Please choose 1-4.")
    except ValueError:
        print("Invalid input.")
        


