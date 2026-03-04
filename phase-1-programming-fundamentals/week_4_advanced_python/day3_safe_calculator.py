try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation(+ - * /): ")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        print("Result:", num1 / num2)

    else:
        print("Invalid operation")

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")