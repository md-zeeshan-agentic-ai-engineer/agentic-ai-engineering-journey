# 07. Count vowels in string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Hello World"))


# reverse_string

def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello"))