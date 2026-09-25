# PHASE 2 — MACHINE LEARNING

## WEEK 20 — DECISION TREES

### DAY 5 — OVERFITTING & HYPERPARAMETERS

**Language: Fully American English**

You are now at one of the most important parts of Decision Trees: controlling model complexity.

A Decision Tree is powerful because it can learn very complicated decision boundaries. But that same flexibility can cause overfitting.

---

# DAY 5 — Overfitting & Hyperparameters

This is one of the most important days of Week 20.

Decision Trees can easily become extremely complex.

## Example

### Small tree

Small Tree

↓

Underfitting

while:

### Huge tree

↓

Memorizes training data

↓

Overfitting

---

# DAY 5 OBJECTIVE

By the end of today, you should be able to:

- Explain **underfitting vs. overfitting**
- Understand why Decision Trees overfit
- Control tree complexity
- Understand the most important Decision Tree hyperparameters
- Compare training and test performance
- Tune a Decision Tree manually
- Understand the role of `max_depth`
- Understand `min_samples_split`
- Understand `min_samples_leaf`
- Understand `criterion`
- Recognize when a tree is too simple or too complex

---

# 1. UNDERFITTING VS. OVERFITTING

Think of a Decision Tree as a student learning from examples.

## Very small tree

Small Tree

↓

Too Simple

↓

Underfitting

The model hasn't learned enough.

### Typical behavior:

```text
Training Performance → Low
Test Performance     → Low
```

It has **high bias**.

---

## Extremely large tree

Huge Tree

↓

Learns tiny details

↓

Memorizes training data

↓

Overfitting

### Typical behavior:

```text
Training Performance → Very High
Test Performance     → Much Lower
```

It has **high variance**.

---

# The goal

We want:

```text
Too Simple          Good Complexity          Too Complex
     ↓                     ↓                      ↓
Underfitting        Generalization          Overfitting
```

The goal of ML is not to maximize training performance.

The goal is to build a model that generalizes to unseen data.

---

# 2. WHY DECISION TREES OVERFIT

Suppose we have:

```text
1000 training samples
```

A Decision Tree can keep splitting:

```text
Root
  ↓
Split
  ├─ Split
  │   ├─ Split
  │   │   ├─ Split
  │   │   └─ Split
  │   └─ Split
  └─ Split
      ├─ Split
      └─ Split
```

Eventually, the tree can create very specific rules for individual training examples.

For example:

```text
IF age > 31
AND income < 42,000
AND feature_3 > 7.4
AND feature_5 <= 1.2
THEN class = 1
```

That rule may work extremely well on the training dataset.

But it may not generalize to new data.

---

# Study these parameters

## `max_depth`

Controls maximum tree depth.

## `min_samples_split`

Minimum samples required to split a node.

## `min_samples_leaf`

Minimum samples allowed in a leaf.

## `criterion`

Understand:

```text
gini
entropy
log_loss
```

You don't need to master every implementation detail yet, but you should understand what the parameters control.


# 3. THE MOST IMPORTANT HYPERPARAMETER

## `max_depth`

This controls the **maximum depth of the tree**.

### Example:

```python
DecisionTreeClassifier(max_depth=3)
```

means:

> Don't allow the tree to grow beyond a depth of 3.

---

## Conceptually:

### `max_depth = 2`

```text
        Root
       /    \
      A      B
```

Very simple.

### `max_depth = 10`

```text
        Root
       /    \
      ...  ...
      /      \
many splits  many splits
```

Much more complex.

---

## General relationship

```text
Smaller max_depth
        ↓
Simpler model
        ↓
Lower overfitting risk
        ↓
But potentially underfitting
```

Whereas:

```text
Larger max_depth
        ↓
More complex model
        ↓
Higher overfitting risk
        ↓
Potentially better training performance
```

---

# 4. `min_samples_split`

This determines the **minimum number of samples required to split an internal node**.

### Example:

```python
DecisionTreeClassifier(min_samples_split=10)
```

A node needs at least 10 samples before the algorithm can consider splitting it.

## Smaller value

```text
min_samples_split = 2
        ↓
More splitting allowed
        ↓
More complex tree
        ↓
Higher overfitting risk
```

## Larger value

```text
min_samples_split = 20
        ↓
Fewer splits
        ↓
Simpler tree
        ↓
Lower complexity
```

---

# 5. `min_samples_leaf`

This determines the **minimum number of training samples allowed in a leaf node**.

### Example:

```python
DecisionTreeClassifier(min_samples_leaf=5)
```

Every final leaf must contain at least 5 samples.

This is a very useful way to prevent the tree from creating tiny leaves.

## Without sufficient restriction:

```text
Leaf
  ↓
1 sample
```

The tree may effectively memorize that sample.

## With:

```python
min_samples_leaf=10
```

you force leaves to contain at least 10 samples.

That generally makes the tree smoother and less sensitive to individual observations.

---

# 6. `criterion`

The criterion determines how the tree evaluates potential splits.

For classification, you should understand:

```text
gini
entropy
log_loss
```

## Gini

```python
criterion="gini"
```

Measures impurity using the Gini criterion.

## Entropy

```python
criterion="entropy"
```

Uses information entropy.

## Log loss

```python
criterion="log_loss"
```

Uses logarithmic loss.

At your current level, you do not need to memorize every mathematical implementation detail.

You should understand:

> The criterion influences how the tree decides which split is better.


# 11. IMPORTANT MENTAL MODEL

Remember this:

```text
MODEL COMPLEXITY
        ↑
        |
Simple -----------+----------- Complex
   |                              |
Underfitting                  Overfitting
   |                              |
Bias ↑                       Variance ↑
```

Hyperparameters are basically controls for model complexity.


# 13. YOUR RESULTS TABLE

Create a table like:

| Model | max_depth | min_samples_split | min_samples_leaf | Train Accuracy | Test Accuracy |
|---|---:|---:|---:|---:|---:|
| A | None | 2 | 1 | — | — |
| B | 3 | 2 | 1 | — | — |
| C | 5 | 2 | 1 | — | — |
| D | 5 | 10 | 5 | — | — |
| E | 10 | 10 | 5 | — | — |

Fill in the actual values from your experiments.


# 15. ⚠️ VERY IMPORTANT

Do not choose hyperparameters based only on training accuracy.

**Bad reasoning:**

> "This model has 99.9% training accuracy, so it's better."

**Better reasoning:**

> "This model achieves strong generalization on unseen validation/test data while controlling unnecessary model complexity."

That mindset will become extremely important when you reach:

**Deep Learning → LLMs → Agentic AI → Research-level ML.**


# 🏆 DAY 5 SUCCESS CRITERIA

You can mark Day 5 complete when you can explain this without notes:

> "A Decision Tree can overfit when it becomes too complex and starts modeling noise or highly specific patterns in the training data. Hyperparameters such as `max_depth`, `min_samples_split`, and `min_samples_leaf` control tree complexity. I should select their values based on generalization performance rather than training performance alone."

If you can explain that and demonstrate it experimentally in your notebook, Day 5 is complete.
