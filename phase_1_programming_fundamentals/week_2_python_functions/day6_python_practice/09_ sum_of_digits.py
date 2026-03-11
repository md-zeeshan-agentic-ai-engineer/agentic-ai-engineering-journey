# 09. Sum of digits

def sum_of_digits(n):
    n = abs(n)  # handle negative numbers
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
        
    return total


# test
num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))
