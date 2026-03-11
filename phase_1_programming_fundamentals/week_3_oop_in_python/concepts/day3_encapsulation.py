# Mini Practice Task for understanding Private Variables (_ concept)

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable (double underscore)

    def show_balance(self):
        print("Current Balance:", self.__balance)

account1 = BankAccount("Zeeshan", 100000000)

account1.show_balance()

# Direct access try kro
print(account1.__balance)

print(account1._BankAccount__balance)
#####################################################
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Gatter
    def get_balance(self):
        return self.__balance
    
    # Setter
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = new_balance

account1 = BankAccount("MD ZEESHAN", 1000)

# Getter use
print(account1.get_balance())

# Setter use
account1.set_balance(2000)
print(account1.get_balance())

# Wrong value
account1.set_balance(-3000)

####################################################

# Marks update function using encapsulation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter with validation
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! 0–100 allowed.")

    # Build: update function
    def update_marks(self, delta):
        new_marks = self.__marks + delta
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Update rejected! Final marks must be 0–100.")


# Test
s1 = Student("Zeeshan", 80)

print(s1.get_marks())   # 80

s1.update_marks(10)
print(s1.get_marks())   # 90

s1.update_marks(-200)   # reject
print(s1.get_marks())   # 90