from storage import load_data, save_data
from utils import add_expense, show_expenses, total_expense, search_category

data = load_data()

while True:

    print("\n1 Add Expense")
    print("2 Show Expenses")
    print("3 Total Expense")
    print("4 Search by Category")
    print("5 Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            amount = float(input("Amount: "))
        except:
            print("Invalid amount")
            continue

        category = input("Category: ")

        data = add_expense(data, amount, category)
        save_data(data)

    elif choice == "2":
        show_expenses(data)

    elif choice == "3":
        total_expense(data)

    elif choice == "4":
        category = input("Enter category: ")
        search_category(data, category)
    
    elif choice =="5":
        break