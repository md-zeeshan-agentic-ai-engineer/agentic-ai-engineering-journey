#             Learn Section
#                         1. List
# a. Mutable(changeable):
# Example 1:Value change karna
nums = [10, 20, 30]
nums[1] = 99
print(nums)
#Example 2: New item add karna
nums = [1, 2, 3]
nums.append(4)
print(nums)
#Example 3: Item remove karna
nums = [5, 6, 7]
nums.remove(6)
print(nums)
# b. Ordered(index-based access)
#Example 1: Index access
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[1])
#Example 2: Negative indexing
fruits = ["apple", "banana", "mango"]
print(fruits[-1])
print(fruits[-2])
#Example 3: Order same rehta hai
nums = [3, 1, 5, 2]
print(nums)
# c. Allow duplicates
#Example 1: Duplicate values
nums = [1, 2, 2, 3, 4, 4]
print(nums)
#Example 2: Count duplicates
nums = [1, 2, 2, 3, 2]
print(nums.count(2))
#Example 3: Duplicate strings
names=["Ali","Zeeshan","Ali"]
print(names)
#Common List Methods (MOST IMPORTANT)
#1️⃣ append() – Last me add karta hai
nums = [1, 2, 3]
nums.append(4)
print(nums)
#2️⃣ insert() – Specific index pe add
nums = [1, 2, 3]
nums.insert(1, 99)
print(nums)
#3️⃣ pop() – Item remove (by index)
nums=[10,20,30,40]
nums.pop(3)
print(nums)
#4️⃣ remove() – Value remove karta hai
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)
#5️⃣ sort() – Order me lagata hai
nums = [3, 1, 4, 2]
nums.sort()
print(nums)
#6️⃣ reverse() – List ulta karta hai
nums = [1, 2, 3]
nums.reverse()
print(nums)
#List Slicing (start:end:step)
#Syntax:
#list[start : end : step]
#1️⃣ Basic slicing
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])
#2️⃣ Start ya End skip karna
print(nums[:3])   # start se
print(nums[3:])   # end tak
#3️⃣ Step use karna
nums=[0,1,2,3,4,5,6,7]
print(nums[::2])
#4️⃣ Reverse list (MOST ASKED)
nums=[0,1,2,3,4,5]
print(nums[::-1])
#5️⃣ Copy list safely
nums=[1,2,3,4,5]
copy_nums = nums[:]
#                         2. Tuple
t=(20,30,40)
print(t)
#1️⃣ Immutable (MOST IMPORTANT)
#❌ Change allowed nahi
t = (1, 2, 3)
t[0] = 10   # ❌ Error
#2️⃣ Ordered (Index-based access)
t = ("a", "b", "c")
print(t[0])
print(t[-1])
#✅ Tuple Unpacking (BONUS but important)
point = (3, 4)
x, y = point
print(x, y)
