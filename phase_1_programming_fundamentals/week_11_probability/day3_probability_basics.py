import random

# coin toss simulation
results = [random.choice(['H','T']) for _ in range(1000)]
print(results.count('H')/1000)
