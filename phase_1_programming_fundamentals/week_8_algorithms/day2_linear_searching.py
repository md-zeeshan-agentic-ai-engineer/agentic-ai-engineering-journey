# linear_searching.py

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search([10,20,30], 40))
print(linear_search([5], 5))