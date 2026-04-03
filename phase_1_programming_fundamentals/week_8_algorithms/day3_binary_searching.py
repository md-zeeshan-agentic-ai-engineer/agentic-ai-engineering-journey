# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) // 2   # IMPORTANT(integer division)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1

arr = [1,3,5,7,9,11]
target = 7

result = binary_search(arr, target)
print(result)


# First Occurrence
def first_occurrence(arr, target):
    low, high = 0, len(arr) -1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1    # LEFT move
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans

arr = [1,2,2,2,3,4]
print(first_occurrence(arr, 2))


# Last Occurrence
def last_occurrence(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans

arr = [1,2,2,2,3,4]
print(last_occurrence(arr, 2))



# Binary Search on Answers

# 1. Koko Eating Bananas
def can_finish(arr, h, k):
    time = 0
    for bananas in arr:
        time += (bananas + k - 1) // k
    return time <= h

def min_speed(arr, h):
    low, high = 1, max(arr)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        if can_finish(arr, h, mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans

arr = [3, 6, 7, 11]
h = 8

print(min_speed(arr, h))


# 2. Minimum days to make bouquet
def can_make(bloomDay, m, k, day):
    count = 0
    bouquets = 0

    for bloom in bloomDay:
        if bloom <= day:
            count += 1
            if count == k:
                bouquets += 1
                count = 0
            else:
                count = 0

    return bouquets >= m

def min_days(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1
    
    low = min(bloomDay)
    high = max(bloomDay)
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if can_make(bloomDay, m, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1

print(min_days(bloomDay, m, k))


# 3. Allocate books
def can_allocate(arr, students, max_pages):
    count = 1
    pages = 0

    for book in arr:
        if pages + book <= max_pages:
            pages += book
        else:
            count += 1
            pages = book

    return count <= students

def allocate_books(arr, students):
    if students > len(arr):
        return -1
    
    low = max(arr)
    high = sum(arr)
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(arr, students, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

arr = [12, 34, 67, 90]
students = 2
print(allocate_books(arr, students))


# 4. Ship packages within days
def can_ship(weights, days, capacity):
    day_count = 1
    current = 0

    for w in weights:
        if current + w <= capacity:
            current += w
        else:
            day_count += 1
            current = w

    return day_count <= days

def ship_packages(weights, days):
    low = max(weights)
    high = sum(weights)
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if can_ship(weights, days, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(ship_packages(weights, days))