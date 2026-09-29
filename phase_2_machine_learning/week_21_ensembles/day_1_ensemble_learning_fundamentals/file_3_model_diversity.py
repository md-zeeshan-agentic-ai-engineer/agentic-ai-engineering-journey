# 13. Mini Experiment — How Diversity Matters

from collections import Counter


def majority_vote(predictions):
    return Counter(predictions).most_common(1)[0][0]


high_agreement = [
    "wrong",
    "wrong",
    "wrong",
    "wrong",
    "wrong"
]

diverse_errors = [
    "wrong",
    "correct",
    "correct",
    "correct",
    "correct"
]

print("High agreement:")
print(high_agreement)
print("Final:", majority_vote(high_agreement))

print("\nDiverse errors:")
print(diverse_errors)
print("Final:", majority_vote(diverse_errors))