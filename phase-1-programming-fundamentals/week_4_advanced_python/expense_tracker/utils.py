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