# 1. Core Concept (must know)

try:
    x=int(input("Enter number "))
    result=10/x

except ValueError:
    print("Input number nhi hai")

except ZeroDivisionError:
    print("Zero se divide nhi hota")

except Exception as e:
    print("Unknown error:",e)

else:
    print("result:",result)

finally:
    print("program execution complete")
    


# 3. Build Project : Safe Calculator

def safe_calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError("Invalid operator")

        print("Result:", result)

    except ValueError as ve:
        print("Value Error:", ve)
    except ZeroDivisionError as ze:
        print("Math Error:", ze)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("Calculator finished")

safe_calculator()


