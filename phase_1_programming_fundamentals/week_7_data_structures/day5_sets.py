# sets.py

# Core Operations

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)
print(a & b)
print(a - b)

# Important Methods

# 1. add() -> add element
s = {1, 2, 3}
s.add(4)

print(s)

# 2. remove() -> remove element(risky)
s = {1, 2, 3}
s.remove(2)

print(s)

# 3. discard() -> remove element (safe)
s = {1, 2, 3}
s.discard(3)

print(s)

# 4. union() -> combine (same as |)
a = {1, 2}
b = {2, 3}

print(a.union(b))

# 5. intersection() -> common (same as &)
a = {1, 2}
b = {2, 3}

print(a.intersection(b))


# Practice

# 1. Remove Duplicates(MOST IMPORTANT)
arr = [1, 2, 2, 3, 4, 4]
unique = list(set(arr))
print(unique)

# 2. Intersection of Two Lists
a = [1, 2, 3]
b = [2, 3, 4]
print(list(set(a) & set(b)))

# 3. Check Common Elements
a = [1, 2, 3]
b = [4, 5, 6]
print(bool(set(a) & set(b)))
