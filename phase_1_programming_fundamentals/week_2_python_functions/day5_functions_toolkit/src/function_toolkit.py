from functions import add, multiply

def run_calculator():
    print("Simple Calculator Toolkit")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Add:", add(a, b))
    print("Multiply:", multiply(a, b))
