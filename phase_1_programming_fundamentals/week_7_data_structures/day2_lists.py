# 1. append()

arr = [1, 2, 3, 4]
arr.append(5)

print(arr)


# 2. remove()

arr = [1, 2, 4, 3, 4, 5]
arr.remove(4)

print(arr)


# 3. pop()

arr = [10, 20, 30, 40, 50]
arr.pop(1)

print(arr)


# 4. sort()

arr = [1, 3, 2, 1, 0, 5, 7, 4, 3, 8, 9]
arr.sort()

print(arr)


# 5. Reverse List

# Method 1 -> Built-in

arr = [1, 2, 3, 4, 5]

arr.reverse()

print(arr)


# Method 2 -> Loop

arr = [2, 5, 7, 8, 9]

reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)


# Method 3 -> Slicing

arr = [4, 6, 7, 8, 9]

reversed_arr = arr[::-1]

print(reversed_arr)


# 6. Remove Duplicates (Loop Method)

arr = [1, 2, 2, 3, 4, 4]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print(unique)