# STEP 1: UNDERSTAND BASIC CODE

import numpy as np

data = [1, 2, 3, 4, 5]

print(np.mean(data))
print(np.var(data))


# STEP 2: HANDS-ON PRACTICE

## Task 1: Use own data
import numpy as np

data = [10, 20, 30, 40, 50]

print("Mean:", np.mean(data))
print("Variance:", np.var(data))


## Task 2: Random Data(REAL ML feel)
import numpy as np

data = np.random.randint(1, 100, size = 10)
print("Mean:", np.mean(data))
print("Variance:", np.var(data))


## Task 3: Add Standard Deviation
print("Std Dev:", np.std(data))



# STEP 3: MINI PROJECT("STUDENT MARKS ANALYZER")

import numpy as np

marks = [45, 67, 89, 56, 72, 90]

print("Mean:", np.mean(marks))
print("Variance:", np.var(marks))
print("Std Dev:", np.std(marks))


# STEP 4: TRY THIS EXPERIMENT

import numpy as np

data1 = [10, 10, 10, 10]
data2 = [1, 50, 100, 200]

print(np.var(data1))
print(np.var(data2))