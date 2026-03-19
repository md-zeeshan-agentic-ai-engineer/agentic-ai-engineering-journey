from analyzer import add, subtract, multiply, divide
from utils import parse_number,validate_operation

def calculate(a, b, op):
    if op == "+":
        return add(a,b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    
if __name__=="__main__":
    try:
        a = parse_number(input("Enter first number: "))
        op = validate_operation(input("Enter operation(+, -, *, /): "))
        b = parse_number(input("Enter second number: "))
        result = calculate(a, b, op)
        print("Result: ", result)
    except Exception as e:
        print("Error:", e)
        