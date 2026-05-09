# Task 1: Create line chart of students marks

import matplotlib.pyplot as plt

students = ["MD ZEESHAN", "GHULAM JEELANI", "MD MOHIT", "MD MAHIR", "MD HASNAIN"]
marks = [75, 80, 85, 65, 90]

plt.figure(figsize=(8, 5))

plt.plot(students, marks, color="blue", marker = "o", linewidth=2)

plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()
plt.savefig("line_chart.png")
plt.show()
plt.close()


# Task 2: Create bar chart of subjects vs marks

import matplotlib.pyplot as plt

subjects = ["AI", "ML", "DL", "LLM", "AGENTIC AI"]
marks = [75, 80, 85, 90, 95]

plt.figure(figsize=(8, 5))

plt.bar(subjects, marks, color="green")

plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.grid()
plt.savefig("bar_chart.png")
plt.show()
plt.close()


# Task 3: Scatter Plot of Random Numbers

import matplotlib.pyplot as plt

x = [1, 3, 4, 6, 7, 8, 18]
y = [3, 6, 8, 9, 0, 0, 30]

plt.figure(figsize=(8, 5))

plt.scatter(x, y, color="red", s=100)

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()
plt.savefig("scatter_plot.png")
plt.show()
plt.close()