# problems.py


# Problem 1: Two Sum

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([2, 7, 11, 15]), 9)


# Problem 2: Reverse String

def reverse_string(s):
    return s[::-1]

print(reverse_string("zeeshan"))


# Problem 3: Find Duplicates

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([1, 3, 4, 3, 3, 5, 2, 2]))


# Problem 4: Frequency Count

def frequency(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq

print(frequency([1, 2, 3, 4, 2, 3, 4, 2, 1, 1, 0, 0, 8]))


# Problem 5: Second Largest Element

def second_largest(arr):
    arr = list(set(arr))    # remove duplicates
    arr.sort()
    return arr[-2]

print(second_largest([24,5,6,7,78]))