# DAY 4 — Random Forest Experiment

Use a classification dataset.

## Train:

Decision Tree

vs

Random Forest

## Compare:

| Model | Train Accuracy | Test Accuracy | Notes |
|---|---|---|---|
| Decision Tree | ... | ... | ... |
| Random Forest | ... | ... | ... |

## Then experiment with:

```text
n_estimators = 10
n_estimators = 50
n_estimators = 100
n_estimators = 200
```

## Also experiment with:

```text
max_depth
```

## Your goal

Do not simply report:

> Random Forest got 94%.

### Explain:

> Why did the ensemble behave differently from the single Decision Tree?

That explanation is the real learning outcome.


# Phase 2 — Week 21 — Day 4

## Random Forest Experiment 🌲🌲🌲

**Today’s Core Focus:** Random Forest  
**Phase:** Machine Learning  
**Week:** 21 — Ensembles  
**Language:** Fully English  

## 🎯 Day 4 Objective

Today you will understand why Random Forest behaves differently from a single Decision Tree, not just learn how to call `RandomForestClassifier`.

Your final learning outcome should be:

> Understand how combining many randomized Decision Trees can improve generalization and reduce the weaknesses of a single tree.

## 1. Warm-up: Decision Tree vs Random Forest

Use the same classification dataset for both models.

### Train:

1. `DecisionTreeClassifier`
2. `RandomForestClassifier`

Use the same:

- train/test split
- features
- target
- evaluation metric

Create this comparison:

| Model | Train Accuracy | Test Accuracy | Observation |
|---|---|---|---|
| Decision Tree | — | — | — |
| Random Forest | — | — | — |

## Important

Do not try to make Random Forest win artificially.

Your job is to understand why the results are different.


## 2. Random Forest Experiment

### Start with:

```python
RandomForestClassifier(
    n_estimators=10,
    random_state=42
)
```

### Then repeat with:

```text
n_estimators = 10
n_estimators = 50
n_estimators = 100
n_estimators = 200
```

### Record the results:

| n_estimators | Train Accuracy | Test Accuracy | Notes |
|---:|---:|---:|---|
| 10 | — | — | — |
| 50 | — | — | — |
| 100 | — | — | — |
| 200 | — | — | — |

### Question

As the number of trees increases:

- Does test accuracy change?
- Does it stabilize?
- Does training become slower?
- Does adding more trees always produce a large improvement?

Write your observations.


## 3. Experiment With `max_depth`

Now keep `n_estimators=100` and experiment with:

```text
max_depth = 2
max_depth = 4
max_depth = 6
max_depth = 10
max_depth = None
```

### Create:

| max_depth | Train Accuracy | Test Accuracy | Interpretation |
|---:|---:|---:|---|
| 2 | — | — | — |
| 4 | — | — | — |
| 6 | — | — | — |
| 10 | — | — | — |
| None | — | — | — |

Your goal is to observe the relationship between:

**model complexity → training performance → generalization**

# 4. The Most Important Concept 🔴

Do not write only:

> "Random Forest got 94%."

Instead answer:

**Why can Random Forest behave differently from a single Decision Tree?**

Your explanation should cover these concepts:

## A. Multiple Trees

A Random Forest contains many Decision Trees.

Instead of relying on one tree:

```text
Dataset
   ↓
Tree 1
Tree 2
Tree 3
Tree 4
...
Tree N
   ↓
Combined prediction
```

## B. Bootstrap Sampling

Different trees can be trained using different samples of the training data.

This creates diversity between trees.

## C. Random Feature Selection

Random Forest also introduces randomness in feature selection when splitting nodes.

Therefore, individual trees do not necessarily learn exactly the same structure.

## D. Aggregation

For classification, the trees collectively vote on the prediction.

Conceptually:

```text
Tree 1 → Class A
Tree 2 → Class A
Tree 3 → Class B
Tree 4 → Class A
Tree 5 → Class A

Final prediction → Class A
```

This collective decision can be more robust than relying on one tree.

# 5. The Key Insight

Write this in your notebook in your own words:

> A single Decision Tree can be highly sensitive to the training data. Random Forest reduces this sensitivity by combining many diverse trees and aggregating their predictions.

Then explain why diversity matters.

This is the real learning objective of today’s session.

# 6. Mini Investigation 🔬

Run one additional experiment.

Compare:

```text
Decision Tree

vs

Random Forest with 10 trees

vs

Random Forest with 100 trees

vs

Random Forest with 200 trees
```

Then answer:

## Question 1

Which model has the highest training accuracy?

## Question 2

Which model has the highest test accuracy?

## Question 3

Does higher training accuracy automatically mean better generalization?

## Question 4

What happens to performance as more trees are added?

## Question 5

Why might 200 trees not be dramatically better than 100 trees?

# Final Learning Explanation

## Why did Random Forest behave differently from a single Decision Tree?

Write this in your notebook:

> A single Decision Tree can become highly dependent on the training data and may overfit by creating very specific decision rules. Random Forest combines many different Decision Trees trained with randomness in samples and features, then aggregates their predictions. This reduces the influence of any single tree and usually improves generalization.

## In our experiment

Your results were:

```text
Decision Tree
Train: 96.35%
Test : 55.31%

Random Forest
Train: 96.35%
Test : 59.78%
```

So:

**Same training accuracy → different test accuracy**

This is important because the test set tells us more about **generalization**.

# Why does Random Forest help? 💡

Think of it like this:

## Single Decision Tree

```text
Training Data
     ↓
 One Tree
     ↓
 Prediction
```

If that tree learns some patterns too specifically, its performance on unseen data can suffer.

## Random Forest

```text
              ┌─ Tree 1 ─┐
              ├─ Tree 2 ─┤
Training ─────┼─ Tree 3 ─┼──→ Voting → Prediction
              ├─ Tree 4 ─┤
              └─ Tree N ─┘
```

Each tree gets some randomness, so the trees are **not identical copies**.

Their predictions are then combined.

# 🎯 Your Real Learning Outcome

Write this as the final conclusion:

> Random Forest is an ensemble method that improves robustness by combining multiple diverse Decision Trees. The individual trees may make different errors, but aggregating their predictions can reduce the impact of those errors and improve generalization.

# ⭐ One important correction to remember

Do not memorize:

> "Random Forest always gives better accuracy than Decision Tree."

Instead memorize:

> "Random Forest often generalizes better because it combines diverse trees and reduces the impact of individual tree errors."

That's the real Machine Learning understanding you're building.
