def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return"error:division by zero"
    return a/b

print("simple calculator")
print("1. add(a,b)")
print("2. subtract(a,b)")
print("3. multiply(a,b)")
print("4. divide(a,b)")

choice=int(input("Enter choice: (1,4)"))
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

if choice == 1:
    print("Result:",add(a,b))
elif choice == 2:
    print("Result:",subtract(a,b))
elif choice == 3:
    print("Result:",multiply(a,b))
elif choice == 4:
    print("Result:",divide(a,b))
else:
    print("Invalid choice")

    