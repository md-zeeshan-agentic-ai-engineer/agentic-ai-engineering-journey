# =========================
# WEEK 4 - DAY 1
# File Handling Practice
# =========================

# ---- Learn Section ----

# Example: Writing into file
with open("data.txt", "w") as f:
    f.write("Hello AI Engineer")

# Example: Reading from file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)


# ---- Build Section ----
# Take input from user
note = input("\nEnter your note: ")

# Append note into file
with open("notes.txt", "a") as f:
    f.write(note + "\n")

# Read and display all notes
print("\nAll Notes:")
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
