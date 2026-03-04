try:
    filename = input("Enter filename: ")
    file = open(filename, "r")
    content = file.read()
    print("File content: \n", content)
    file.close()

except FileNotFoundError:
    print("File not found. Please check the file name.")

finally:
    print("Program finished")