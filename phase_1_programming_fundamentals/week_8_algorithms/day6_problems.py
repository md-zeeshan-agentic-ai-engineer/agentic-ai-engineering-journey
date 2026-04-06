# Problem 1: Two Sum (Optimized)

# Concept: HashMap / Dictionary
# Goal: O(n)

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i

# Think:

# Time Complexity = O(n)
# Space Complexity = O(n)

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)

##########################################

# Problem 2: Binary Search Problem

# Concept: Divide & Conquer

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

#Complexity: O(log n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = binary_search(arr, target)
print(result)

arr = [1, 6, 2, 8, 0, 4, 6, 7, 8, 9]
arr.sort()
target = 6
result = binary_search(arr, target)
print(result)

###########################################

# Problem 3: Sort + Find Element

# Concept: Sorting + Searching combo

# arr.sort()
# then apply binary search

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

arr = [1, 6, 2, 8, 0, 4, 6, 7, 8, 9]
arr.sort()
target = 6
result = binary_search(arr, target)
print(result)

# Complexity:

# Sorting = O(n log n)
# Search = O(log n)
#   Total = O(n log n)

####################################

# Problem 4: Find Missing Number

# Concept: Math Optimization

def missing_number(nums):
    n = len(nums)
    total = n*(n+1)//2
    return total - sum(nums)

# Complexity: O(n) (BEST)

nums = [3, 0,  1]
result = missing_number(nums)
print(result)

######################################

# Problem 5: Maximum Subarray (Kadane’s Algorithm)

# Concept: Dynamic Programming

def max_subarray(nums):
    current = nums[0]
    maximum = nums[0]
    
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        maximum = max(maximum, current)
        
    return maximum

# Complexity: O(n)

nums = [-2,1,-3,4,-1,2,1,-5,4]

result = max_subarray(nums)
print(result)