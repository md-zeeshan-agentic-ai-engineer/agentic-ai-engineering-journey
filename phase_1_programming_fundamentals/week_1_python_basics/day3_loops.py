#####################               for loop             ####################

#Basic syntax
#for variable in sequence:
#    code
#Example:
for i in range(5):
    print(i)
range()
for i in range(1, 6):
    print(i)
for i in range(1, 10, 2):
    print(i)
for i in range(3):
    print("Hello")

#Example 1: 1 se 10 print karo
for i in range(1, 11):
   print(i)

#Example 2: Even numbers (1–20)
for i in range(2, 21, 2):
    print(i)

#Example 3: Table of 5
for i in range(1, 11):
    print(5 * i)

###############               while loop               ###############

#Basic Syntax
#while condition:
#   code


#Output:
1
2
3
4
5

#Step-by-step samjhiye
i = 1
while i <= 3:
    print("Hello")
    i += 1


#i = 1 → condition true → print
#i = 2 → condition true → print
#i = 3 → condition true → print
#i = 4 → condition false → loop stop

#Common Examples
#Example 1: 1 se 10 print
i = 1
while i <= 10:
    print(i)
    i += 1

#Example 2: Even numbers (1–20)
i = 2
while i <= 20:
    print(i)
    i += 2

#Example 3: User se input jab tak sahi na ho
password = ""

while password != "python":
    password = input("Enter password: ")

print("Access granted")

####################            #Pattern printer                 ####################
#Pattern 1: Simple Star Pattern
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()

#Pattern 2: Number Pattern
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

#Pattern 3: Reverse Star Pattern
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#Pattern 4: Square Pattern
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()
