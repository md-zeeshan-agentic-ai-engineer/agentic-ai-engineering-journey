# 1. String

text = "Zeeshan"


# 2. Indexing

text = "Zeeshan"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])
print(text[-5])


# 3. Slicing

text = "Zeeshan"

print(text[0:4])
print(text[:4])
print(text[2:])
print(text[::-1])
print(text[::2])
print(text[::-2])
print(text[::3])
print(text[::-3])


# 4. VERY IMPORTANT METHODS

text = " hello world "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("world", "AI"))
print(text.split())


# 5. Palindrome Check

text = "madam"

if text == text[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")


# 6. Count Vowels

text = "Zeeshan"
vowels = "aeiou"

count = 0
for ch in text:
    if ch in vowels:
        count += 1

print(count)


# 7. Word Count

text = "I love AI and AI loves me"

words = text.split()
print(len(words))