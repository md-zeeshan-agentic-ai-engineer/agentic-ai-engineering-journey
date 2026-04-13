# Day 3 - Derivative Intuition

import numpy as np

# Function 1: x^2
def f1(x):
    return x**2

def df1(x):
    return 2*x


# Function 2: x^3
def f2(x):
    return x**3

def df2(x):
    return 3*(x**2)


# Function 3: sin(x)
def f3(x):
    return np.sin(x)

def df3(x):
    return np.cos(x)


# Test points
points = [-2, 0, 2]

print("Function: x^2")
for x in points:
    print(f"x={x}, slope={df1(x)}")

print("\nFunction: x^3")
for x in points:
    print(f"x={x}, slope={df2(x)}")

print("\nFunction: sin(x)")
points_sin = [0, np.pi/2, np.pi]
for x in points_sin:
    print(f"x={x:.2f}, slope={df3(x):.2f}")