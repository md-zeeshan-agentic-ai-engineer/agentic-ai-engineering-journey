# 11. HANDS-ON — Manual Voting Ensemble
## Now create a simple Python experiment.


from collections import Counter

predictions = [
    "cat",
    "cat",
    "dog",
    "cat",
    "cat"
]

vote_counts = Counter(predictions)

final_prediction = vote_counts.most_common(1)[0][0]

print("Individual predictions:")
for i, prediction in enumerate(predictions, start=1):
    print(f"Model {i}: {prediction}")

print("\nVote counts:")
print(vote_counts)

print("\nFinal prediction:", final_prediction)