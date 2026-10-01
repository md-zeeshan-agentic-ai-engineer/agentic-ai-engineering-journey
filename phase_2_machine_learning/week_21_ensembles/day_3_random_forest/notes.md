# 🗓️ DAY 3 — Random Forest 🌲🌲🌲

Random Forest is one of your most important Week 21 topics.

## Conceptually:

```text
                         Dataset
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
           Tree 1        Tree 2        Tree 3
              ↓             ↓             ↓
              └─────────────┼─────────────┘
                            ↓
                      Aggregation
                            ↓
                      Final Output
```

Random Forest introduces randomness in two important places:

### 1. Random observations

Different trees can see different bootstrap samples.

### 2. Random features

At a split, a tree considers a random subset of features.

This helps make the trees less correlated.

# 🔥 Random Forest — Core Parameters

You should understand:

```python
from sklearn.ensemble import RandomForestClassifier
```

Important parameters:

```text
n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features
random_state
```

## n_estimators

Number of trees.

Example:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

More trees generally improve stability up to a point, but increase computation.


# PHASE 2 — MACHINE LEARNING

## WEEK 21 — ENSEMBLE LEARNING

### DAY 3 — RANDOM FOREST 🌲🌲🌲

Today we continue from Day 2: Decision Trees and learn Random Forest properly.

The goal is not just to memorize `RandomForestClassifier`. You should understand why Random Forest works, what randomness it introduces, and how its important parameters affect the model.

## 1. Today's Learning Objective

By the end of Day 3, you should be able to:

- Explain what Random Forest is
- Explain how multiple Decision Trees work together
- Understand Bootstrap Sampling
- Understand Random Feature Selection
- Understand Aggregation / Voting
- Understand the difference between a Decision Tree and Random Forest
- Understand these parameters:

```text
n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features
random_state
```

- Train a Random Forest classifier with Scikit-learn
- Compare different parameter settings
- Understand why Random Forest usually generalizes better than a single Decision Tree

## 2. First Understand the Big Picture

A single Decision Tree looks like:

```text
Dataset
↓
One Decision Tree
↓
Prediction
```

Random Forest looks like:

```text
                         Dataset
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
           Tree 1        Tree 2        Tree 3
              ↓             ↓             ↓
           Class A       Class B       Class A
              └─────────────┼─────────────┘
                            ↓
                       Aggregation
                            ↓
                      Final Output
```

Imagine 100 people independently solving the same problem.

Instead of trusting one person:

```text
Person 1 → A
```

you ask 100 people:

```text
Person 1 → A
Person 2 → B
Person 3 → A
Person 4 → A
...
Person 100 → A
```

Then use the majority decision:

```text
A = 73 votes
B = 27 votes

Final prediction = A
```

That is the basic intuition behind Random Forest classification.

## 3. Why Is It Called "Random" Forest?

There are two important sources of randomness.

### Randomness #1 — Random Observations

Different trees can receive different bootstrap samples of the training data.

For example:

```text
Original Dataset

A B C D E F G H
```

Tree 1 might receive:

```text
A B B D E G H H
```

Tree 2:

```text
A C C D F F G H
```

Tree 3:

```text
B B C E F G G H
```

Notice something important:

The samples can contain duplicates.

This is called sampling with replacement.

### Randomness #2 — Random Features

Suppose your dataset has:

```text
Age
Salary
Experience
Education
Location
Credit Score
```

A normal Decision Tree can consider all available features when searching for a split.

Random Forest does something different.

At a particular split, it may randomly consider only:

```text
Age
Experience
Credit Score
```

instead of all six.

At another split:

```text
Salary
Education
Location
```

may be considered.

This makes the trees less correlated with each other.
# Random Forest — Notes

## 5. Why Do We Want Trees to Be Less Correlated?

This is one of the most important ideas today.

Suppose you have 100 trees, but every tree behaves almost exactly the same:

```text
Tree 1 → A
Tree 2 → A
Tree 3 → A
Tree 4 → A
...
Tree 100 → A
```

You don't get much benefit from having 100 trees.

But if the trees make somewhat different errors:

```text
Tree 1 → A
Tree 2 → B
Tree 3 → A
Tree 4 → A
Tree 5 → B
...
```

their mistakes can partially cancel each other when combined.

So Random Forest tries to create:

**Many strong but diverse Decision Trees.**

This is a core Ensemble Learning principle.

---

## 6. Final Prediction — Voting

For classification, Random Forest generally uses **majority voting**.

Suppose we have 7 trees:

```text
Tree 1 → Spam
Tree 2 → Not Spam
Tree 3 → Spam
Tree 4 → Spam
Tree 5 → Spam
Tree 6 → Not Spam
Tree 7 → Spam
```

Votes:

```text
Spam     = 5
Not Spam = 2
```

Therefore:

```text
Final Prediction = Spam
```

---

## 7. The Main Random Forest Parameters

Now we move to the important practical part.

```python
from sklearn.ensemble import RandomForestClassifier
```

You should understand these six parameters.

### 7.1 n_estimators

**Meaning:**

Number of trees in the forest.

**Example:**

```python
RandomForestClassifier(
    n_estimators=100
)
```

means:

```text
100 Decision Trees
```

Conceptually:

```text
n_estimators = 10
        ↓
10 trees

n_estimators = 100
        ↓
100 trees

n_estimators = 500
        ↓
500 trees
```

Generally, increasing the number of trees can make predictions more stable, but it also increases computation.

**Remember:**

```text
n_estimators = How many trees?
```

---

## 8. max_depth

This controls the maximum depth of each Decision Tree.

**Example:**

```python
RandomForestClassifier(
    max_depth=5
)
```

Each tree can grow up to approximately:

```text
Depth 5
```

A deeper tree:

```text
more complex
    ↓
can capture more patterns
    ↓
but may overfit
```

A shallow tree:

```text
simpler
    ↓
less complex
    ↓
may underfit
```

**Remember:**

```text
max_depth = How deep can each tree grow?
```
# Random Forest Notes

## 9. `min_samples_split`

This controls the minimum number of samples required for a node to be split.

Example:

```python
min_samples_split=10
```

means a node generally needs at least 10 samples before it can be split.

Smaller value:

```text
more splitting
→ more complex trees
```

Larger value:

```text
less splitting
→ simpler trees
```

Remember:

```text
min_samples_split = How many samples are required before splitting a node?
```


## 10. `min_samples_leaf`

This controls the minimum number of samples that must remain in a leaf.

Example:

```python
min_samples_leaf=5
```

means each leaf must contain at least 5 training samples.

This can help prevent trees from creating extremely tiny leaves.

Remember:

```text
min_samples_leaf = Minimum samples allowed in a leaf.
```


## 11. `max_features`

This is particularly important for Random Forest.

It controls how many features are considered when looking for a split.

Suppose:

```text
10 total features
```

At a particular split, Random Forest may consider only a subset.

For example:

```text
Feature 1
Feature 4
Feature 6
Feature 9
```

instead of all 10.

This introduces feature randomness.

Remember:

```text
max_features = How many features can be considered at a split?
```


## 12. `random_state`

You have already seen this in previous weeks.

Example:

```python
random_state=42
```

Random Forest contains randomness.

Setting:

```python
random_state=42
```

makes the random process reproducible.

For example:

```python
model_1 = RandomForestClassifier(random_state=42)
model_2 = RandomForestClassifier(random_state=42)
```

will use the same reproducible random sequence under the same conditions.

Remember:

```text
random_state = Make the randomness reproducible.
```


## 15. Your Mental Model

You should now be able to visualize:

```text
Training Data
      ↓
Bootstrap Sampling
      ↓
 ┌──────────────┬──────────────┬──────────────┐
 ↓              ↓              ↓
Tree 1         Tree 2         Tree 3
 ↓              ↓              ↓
Random         Random         Random
Features       Features       Features
 ↓              ↓              ↓
Prediction     Prediction     Prediction
 └──────────────┴──────────────┴──────────────┘
                    ↓
              Voting / Average
                    ↓
             Final Prediction
```

For classification:

```text
Voting
```

For regression:

```text
Averaging
```
# 16. Decision Tree vs Random Forest

| Concept | Decision Tree | Random Forest |
|---|---|---|
| Number of trees | One | Many |
| Bootstrap samples | No | Yes |
| Random feature selection | No/limited | Yes |
| Diversity | Low | Higher |
| Overfitting risk | Often higher | Usually lower |
| Interpretability | Easier | More difficult |
| Computation | Lower | Higher |
| Prediction | One tree | Aggregated trees |

Don't memorize the table blindly.

Understand the fundamental difference:

- Decision Tree = one model.
- Random Forest = many randomized Decision Trees + aggregation.


# 17. TODAY'S PRACTICAL TASK 🔥

You will create a new notebook:

`week_21_day_3_random_forest.ipynb`

Inside it, implement a Random Forest classifier.

## Required sections:

2. Load Dataset

3. Explore Dataset

4. Train-Test Split

5. Train Random Forest

6. Make Predictions

7. Evaluate Model

8. Experiment with n_estimators

9. Experiment with max_depth

10. Experiment with max_features

11. Compare Results

12. Final Observations


# 18. Experiment 1 — Number of Trees

Train models with:

```python
n_estimators = 10
n_estimators = 50
n_estimators = 100
n_estimators = 200
```

Record:

```text
Number of Trees | Accuracy
10              | ...
50              | ...
100             | ...
200             | ...
```

The purpose is not to find a magical number.

The purpose is to observe:

> What happens when the forest becomes larger?


# 19. Experiment 2 — Tree Depth

Try:

```python
max_depth = 2
max_depth = 5
max_depth = 10
max_depth = None
```

Record the results.

Think about:

```text
Too shallow → Underfitting
Too complex → Potential overfitting
```


# 20. Experiment 3 — Feature Randomness

Try different:

```python
max_features
```

values.

For example:

```python
max_features="sqrt"
```

and another reasonable setting such as:

```python
max_features="log2"
```

Compare the results.
# 21. Important Rule for Today

Do not just run:

```python
RandomForestClassifier()
```

and say:

> "Random Forest completed."

Your target today is to understand:

```text
WHY
↓
Random observations
+
Random features
↓
Different trees
↓
Less correlated trees
↓
Aggregation
↓
Better generalization
```

That chain is much more important than memorizing the API.


# 22. Day 3 Challenge 🔴

Answer these without looking at the notes:

### Q1
Why does Random Forest use multiple Decision Trees?

### Q2
What is bootstrap sampling?

### Q3
Why does Random Forest randomly select features?

### Q4
What does `n_estimators` control?

### Q5
What does `max_depth` control?

### Q6
What is the difference between `min_samples_split` and `min_samples_leaf`?

### Q7
What does `random_state=42` do?

### Q8
For classification, how does Random Forest combine the predictions of its trees?

### Q9
Why is tree diversity important?

### Q10
What is the fundamental difference between a Decision Tree and a Random Forest?


# 23. Day 3 Completion Criteria ✅

Do not mark Day 3 complete until you can explain this in your own words:

> "Random Forest builds many Decision Trees using different bootstrap samples and random subsets of features. The individual trees make predictions, and those predictions are aggregated to produce the final prediction. The randomness makes the trees less correlated, which can improve generalization compared with relying on a single tree."

And you must have:

- Understood bootstrap sampling
- Understood random feature selection
- Understood voting
- Understood all 6 core parameters
- Implemented `RandomForestClassifier`
- Run the `n_estimators` experiment
- Run the `max_depth` experiment
- Run the `max_features` experiment
- Recorded results
- Answered the 10 questions


# 🎯 Day 3 Core Skill

Do not think of Random Forest as a new algorithm that you simply call with one line of Python.

Think:

**Decision Tree → Randomized Trees → Diversity → Aggregation → Ensemble Prediction.**

That is the concept you need to carry forward into the rest of Ensemble Learning.
