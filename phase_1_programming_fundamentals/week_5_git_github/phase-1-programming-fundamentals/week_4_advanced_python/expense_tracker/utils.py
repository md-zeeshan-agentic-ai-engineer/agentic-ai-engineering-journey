def add_expense(data, amount, category):
    expense = {
        "amount": amount,
        "category": category
    }
    data.append(expense)
    return data

def show_expenses(data):
    for expense in data:
        print(expense["amount"], "-", expense["category"])

def total_expense(data):
    total = 0
    
    for expense in data:
        total += float(expense["amount"])
    print("Total Expense:", total)
    
def search_category(data, category):
    for expense in data:
        if expense["category"] == category:
            print(expense["amount"], "-", expense["category"])