# DAY 6 — Classification + Regression Trees

Do not limit your understanding to classification.

## Classification

```text
Features → Decision Tree → Class
```

### Example:

```text
Customer data → BUY / DON'T BUY
```

### Use:

```python
DecisionTreeClassifier
```

## Regression

```text
Features → Decision Tree → Numerical value
```

### Example:

```text
House features → ₹ price
```

### Use:

```python
from sklearn.tree import DecisionTreeRegressor
```

Run one small experiment with each.

-------------------------------------------------------------

# PHASE 2 — MACHINE LEARNING

## WEEK 20 — TREES

### DAY 6 — Classification + Regression Trees

Language: Fully English

Today's goal is to understand Decision Trees for both classification and regression, not just memorize `DecisionTreeClassifier`.

> **Core principle:**
> A Decision Tree repeatedly asks questions about features and uses the answers to reach a prediction.

---

# 🎯 DAY 6 OBJECTIVES

By the end of today, you should be able to:

- Explain how a Decision Tree works
- Understand **root, node, branch, leaf**
- Understand splitting
- Understand **classification trees**
- Understand **regression trees**
- Use `DecisionTreeClassifier`
- Use `DecisionTreeRegressor`
- Understand `max_depth`
- Understand overfitting in trees
- Interpret a simple tree
- Run one classification experiment
- Run one regression experiment

---

# 1. Decision Tree — Core Idea

A tree looks conceptually like this:

```text
                 Feature?
                /        \
              Yes         No
              /            \
         Feature?        Class B
          /    \
        Yes     No
        /        \
    Class A     Class B
```

The model is essentially learning:

```text
IF condition 1
    IF condition 2
        → prediction A
    ELSE
        → prediction B
ELSE
    → prediction C
```

This is why Decision Trees are often relatively easy to interpret.

---

# 2. Important Terminology

Learn these properly.

## Root

The first split in the tree.

```text
        ROOT
       /    \
```

## Node

A decision point.

```text
Feature > 10?
```

## Branch

The path created by a decision.

```text
        Feature > 10?
          /       \
        Yes       No
```

## Leaf

The final prediction.

```text
        /       \
    Class A    Class B
```

---

# 3. Classification Tree

A classification tree predicts a **category/class**.

Examples:

```text
Customer features
        ↓
Decision Tree
        ↓
BUY / DON'T BUY
```

or:

```text
Email features
        ↓
Decision Tree
        ↓
SPAM / NOT SPAM
```

or:

```text
Medical features
        ↓
Decision Tree
        ↓
Class A / Class B
```

The general flow is:

```text
Features
    ↓
Decision Tree
    ↓
Class
```
# 5. What Did We Just Do?

The important pipeline is:

```text
Dataset
    ↓
Train/Test Split
    ↓
DecisionTreeClassifier
    ↓
Fit
    ↓
Predict
    ↓
Evaluate
```

The most important lines are:

```python
model = DecisionTreeClassifier(max_depth=2)
```

then:

```python
model.fit(X_train, y_train)
```

then:

```python
predictions = model.predict(X_test)
```

# 6. Why `max_depth` Matters

This is extremely important.

Suppose we allow the tree to grow without meaningful restrictions:

```text
                    Root
                   /    \
                 /        \
              Node        Node
             /    \      /    \
            ...    ...    ...    ...
```

A very deep tree can memorize the training data.

That creates:

```text
Training performance → very high
Generalization       → poor
```

This is overfitting.

# 7. Experiment With Tree Depth

Change:

```python
max_depth=2
```

to:

```python
max_depth=1
```

Then:

```python
max_depth=3
```

Then:

```python
max_depth=5
```

Observe how the model behaves.

Your objective is not to find a magic number.

Your objective is to understand:

```text
Tree too shallow
        ↓
Underfitting

Tree too deep
        ↓
Overfitting

Appropriate complexity
        ↓
Better generalization
```

# 8. Regression Tree

Now the important second half.

A Decision Tree can also predict a continuous numerical value.

Example:

```text
House features
      ↓
Decision Tree
      ↓
House price
```

The flow becomes:

```text
Features → Decision Tree → Numerical Value
```

Examples:

```text
House size → Price
Age → Salary
Engine size → Car price
Advertising → Sales
```

# 10. Classification vs Regression

Memorize this distinction:

| Task | Model |
|---|---|
| Predict a class | `DecisionTreeClassifier` |
| Predict a number | `DecisionTreeRegressor` |

Examples:

```text
Spam / Not Spam
        ↓
   Classifier
```

```text
House price
      ↓
   Regressor
```

# 11. The Most Important Mental Model

Do not think:

> "Decision Tree is just another sklearn algorithm."

Think:

```text
Decision Tree
       ↓
Learn useful decision boundaries
       ↓
Split data repeatedly
       ↓
Create smaller groups
       ↓
Reach a prediction
```

For classification:

```text
Split → split → split → class
```

For regression:

```text
Split → split → split → numerical prediction
```

# Explain Without Code

Write answers to:

1. What is a Decision Tree?

2. What is a root?

3. What is a node?

4. What is a branch?

5. What is a leaf?

6. What is a classification tree?

7. What is a regression tree?

8. What does `max_depth` control?

9. Why can a deep tree overfit?

10. What is the difference between
    `DecisionTreeClassifier` and
    `DecisionTreeRegressor`?

# Day 6 Core Skill Output

Decision Trees — Classification + Regression

# Day 6 Project Output

Two small tree experiments + one custom experiment

Once these are complete, Week 20 moves toward ensemble methods, where you will learn why combining many trees can be much more powerful than relying on a single tree.
