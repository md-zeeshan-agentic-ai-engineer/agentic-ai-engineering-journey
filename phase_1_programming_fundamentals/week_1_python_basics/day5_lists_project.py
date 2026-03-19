# lists.py

def remove_duplicates(lst):
    return list(set(lst))

def find_max(lst):
    return max(lst)

def reverse_list(lst):
    return lst[::-1]

def sum_list(lst):
    return sum(lst)

numbers = [1, 2, 2, 3, 4, 4, 5]

print("Original:", numbers)
print("No duplicates:", remove_duplicates(numbers))
print("Max:", find_max(numbers))
print("Reversed:", reverse_list(numbers))
print("Sum:", sum_list(numbers))
