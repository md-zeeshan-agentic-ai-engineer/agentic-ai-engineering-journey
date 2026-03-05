from storage import load_data, save_data
from utils import add_expense, show_expenses

data = load_data()

while True:

    print("\n1 Add Expense")
    print("2 Show Expenses")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":

        amount = input("Amount: ")
        category = input("Category: ")

        data = add_expense(data, amount, category)
        save_data(data)

    elif choice == "2":
        show_expenses(data)

    elif choice == "3":
        break