#   Part 1 - Learn: Recursion

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)


def countup(n):
    if n == 0:
        return
    countup(n-1)
    print(n)

countup(10)

#   Part 2 - Build: Factorial + Fibonacci

#   a. Factorial (Recursive)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120

#   b. Fibonacci (Recursive)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")

# Next Level(Optional but powerful)
# Optimized Fibonacci(Memorization - DP)

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])


# 🚀 Part 3 Level Up Tasks (Very Important)
# A. Recursive Thinking Training

# Solve:

# 1. Sum of digits (recursively)

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))

# 2. Reverse a string

def reverse_str(s):
    if len(s) == 0:
        return s
    return reverse_str(s[1:])+s[0]
print(reverse_str("zeeshan"))

# 3. Power(x, n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)
print(power(5, 5))

# 4. GCD using recursion(Euclidean Algorithm)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))   # 6
