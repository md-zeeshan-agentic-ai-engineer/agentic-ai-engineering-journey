# 08. Remove duplicates from list

# Method 1: Using set (order not guaranteed)

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)


# Ab final best version (order maintain + interview ready)

nums = [1, 2, 2, 3, 4, 4, 5]

unique = []
for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)