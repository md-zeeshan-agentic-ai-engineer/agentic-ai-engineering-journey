# arrays_basics

## 1. Indexing

arr = [1, 2, 3, 4, 5]

print(arr[0])
print(arr[1])
print(arr[4])
print(arr[-1])
print(arr[-3])


## 2. Slicing

arr = [1, 2, 3, 4, 5]

print(arr[1:3])
print(arr[:2])
print(arr[::2])
print(arr[::-1])
print(arr[-3:])


## 3. Loop(for loop in array)

### a. Print all elements

arr = [10, 20, 30, 40, 50]

for i in arr:
    print(i)


### b. Multiplay each element

arr = [5, 10, 15, 20, 25]

for i in arr:
    print(i * 2)

### c. Square of each element

arr = [3, 6, 9, 12, 15]

for i in arr:
    print(i * i)

### d. Even numbers

arr = [1, 2, 3, 4, 5]

for i in arr:
    if i % 2 == 0:
        print(i)

### e. Sum

arr = [10, 20, 30, 40, 50]

total = 0
for i in arr:
    total += i
    print("Sum:", total)


### f. Even Sum

arr = [50, 15, 20]

total = 0
for i in arr:
    if i % 2 == 0:
        total += i
print(total)

### g. Max element

arr = [5, 10, 15, 20, 25]

max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i
print(max_val)

### h. Smallest element

arr = [1, 2, 3, 4, 5, 6, 9]

min_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i
print(min_val)