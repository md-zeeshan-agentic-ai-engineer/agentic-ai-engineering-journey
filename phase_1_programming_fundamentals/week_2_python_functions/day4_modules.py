# 1.   Learn
# a. import,from x import y
# Basic
import math
print(math.sqrt(16))

# Specific import
from math import sqrt
print(sqrt(16))

# Alias(real-world use)
import numpy as np
print(np.array([1,2,3]))

# b.  _name_=="_main_"(VERY IMPORTANT)

def add(a, b):
    return a + b

if __name__=="__main__":
    print(add(2, 3))

# c. Custom Modules(Own files)
# Example
# project/  math_utils.py , main.py

#  math_utils.py

def add(a, b):
    return a + b

# ise dusre file(test.py) me le jake test karna hai
# main.py
from math_utils import add
print(add(4, 16))

# d. Week 2 Day 4 - Modules & Structure
# Folder Structure(Agent mindset)
# project/
# │── main.py
# │
# ├── utils/
# │   ├── math_ops.py
# │   └── string_ops.py
# │
# ├── agents/
# │   └── calculator_agent.py

# e. __init__.py(Package maker)
