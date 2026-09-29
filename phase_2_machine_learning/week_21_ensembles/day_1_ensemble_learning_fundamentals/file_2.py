# 12. Upgrade the Experiment
## Now create different prediction scenarios.

from collections import Counter


def majority_vote(predictions):
    counts = Counter(predictions)
    return counts.most_common(1)[0][0]


scenarios = {
    "Scenario 1": ["cat", "cat", "dog", "cat", "cat"],
    "Scenario 2": ["dog", "cat", "dog", "cat", "dog"],
    "Scenario 3": ["cat", "dog", "dog", "cat", "dog"],
}


for name, predictions in scenarios.items():
    result = majority_vote(predictions)

    print(name)
    print("Predictions:", predictions)
    print("Final prediction:", result)
    print()