# PHASE 2 — MACHINE LEARNING

## WEEK 21 — ENSEMBLE METHODS

### DAY 1 — Ensemble Learning Fundamentals

Your Week 21 focus is Ensemble Learning, with the progression:

**Ensemble Fundamentals → Random Forest → Boosting → Model Comparison → Ensemble Project**

Today we will build the foundation before touching Random Forest or Boosting.

---

## 🎯 DAY 1 OBJECTIVES

By the end of today, you should be able to:

1. Explain what **ensemble learning** is.
2. Explain why combining models can improve predictions.
3. Understand **majority voting**.
4. Understand the relationship between **model diversity and ensemble performance**.
5. Distinguish:
   - Bagging
   - Boosting
   - Voting
   - Stacking
6. Understand why Random Forest works.
7. Implement a simple ensemble manually using Python.
8. Understand the difference between:
   - a single Decision Tree
   - multiple Decision Trees
   - an ensemble of different models.

---

# 1. What Is Ensemble Learning?

An ensemble combines predictions from multiple models to produce a final prediction.

Instead of:

```text
Data
  ↓
One Model
  ↓
Prediction
```

we use:

```text
             ┌── Model 1 ──┐
             ├── Model 2 ──┤
Data ────────┼── Model 3 ──┼──→ Combination → Final Prediction
             ├── Model 4 ──┤
             └── Model 5 ──┘
```

Instead of trusting one model completely, we combine multiple models.

---

## Core idea

Many reasonably good models can sometimes produce a stronger and more stable prediction when their errors are not identical.

This is one of the most important ideas in classical machine learning.

---

# 2. Simple Example — Majority Voting

Suppose five models classify an image.

```text
Model 1 → Cat
Model 2 → Cat
Model 3 → Dog
Model 4 → Cat
Model 5 → Cat
```

Count the predictions:

```text
Cat = 4
Dog = 1
```

Therefore:

```text
Final Prediction → Cat
```

This is called **majority voting**.

### Mental model

```text
Model predictions
      ↓
   Voting
      ↓
Most common prediction
      ↓
Final prediction
```

---

# 3. Why Can Ensembles Work?

Suppose one Decision Tree makes an error.

That does not necessarily mean that every other model will make the same mistake.

For example:

```text
Tree 1 → Wrong
Tree 2 → Correct
Tree 3 → Correct
Tree 4 → Correct
Tree 5 → Correct
```

Majority:

```text
Correct = 4
Wrong = 1
```

Final result:

```text
Correct
```

This is why diversity between models matters.

---

# DAY 1 — Why Do Ensembles Work?

Suppose one Decision Tree makes an error.

If several sufficiently different models make independent or partially independent errors, combining them can reduce the impact of individual mistakes.

This connects directly to what you learned in Week 20:

```text
Decision Tree
      ↓
Can have high variance
      ↓
Sensitive to training data
      ↓
Ensemble several trees
      ↓
More stable prediction
```

This leads to Random Forest.

---

# Core intuition

Suppose five models predict:

```text
Model 1 → Cat
Model 2 → Cat
Model 3 → Dog
Model 4 → Cat
Model 5 → Cat
```

Majority vote:

```text
Cat = 4
Dog = 1
```

Final → Cat

This is the basic intuition behind ensemble methods.

# 4. Model Diversity

This is a concept you must understand deeply.

Suppose we have five models:

```text
Model 1
Model 2
Model 3
Model 4
Model 5
```

If all five models make exactly the same mistakes:

```text
Model 1 → Wrong
Model 2 → Wrong
Model 3 → Wrong
Model 4 → Wrong
Model 5 → Wrong
```

An ensemble does not magically fix the problem.

But if their errors differ:

```text
Model 1 → Wrong
Model 2 → Correct
Model 3 → Correct
Model 4 → Correct
Model 5 → Correct
```

combining them can reduce the effect of individual errors.

## Key principle

> Ensemble performance benefits when the individual models are both useful and sufficiently different in their errors.

Do not memorize only:

> “More models = better.”

That is not always true.

The quality and diversity of the models matter.

---

# 5. Connection With Week 20 — Decision Trees

You already learned that Decision Trees can have relatively high variance and can be sensitive to the training data.

Conceptually:

```text
Decision Tree
      ↓
High variance
      ↓
Sensitive to training data
      ↓
One tree may be unstable
```

Now imagine building many trees:

```text
Tree 1
Tree 2
Tree 3
Data ───── Tree 4 ───→ Combine predictions
Tree 5
...
Tree N
```

The combined prediction can be more stable.

This idea leads directly to:

# 🌲 Random Forest

Random Forest is an ensemble of Decision Trees with additional randomness designed to make the trees less correlated.

You will study this more deeply later in Week 21.

---

# 6. Four Important Ensemble Families

You need to know these four concepts.

## A. Bagging

**Bagging = Bootstrap Aggregating**

### Basic idea:

```text
Original Dataset
       ↓
Create different training samples
       ↓
Train multiple models
       ↓
Combine predictions
```

### Example:

```text
Dataset
  ├─ Sample 1 → Tree 1
  ├─ Sample 2 → Tree 2
  ├─ Sample 3 → Tree 3
  ├─ Sample 4 → Tree 4
  └─ Sample 5 → Tree 5
           ↓
       Aggregate
           ↓
    Final Prediction
```

Random Forest is strongly associated with this family.

---

# 7. Boosting

Boosting follows a different philosophy.

Instead of primarily training many models independently, boosting builds models sequentially, with later models focusing on mistakes or difficult examples from earlier stages.

Conceptually:

```text
Model 1
   ↓
Find weaknesses/errors
   ↓
Model 2
   ↓
Focus more on difficult cases
   ↓
Model 3
   ↓
...
   ↓
Final prediction
```

Examples you will encounter later:

- AdaBoost
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

Do not worry about implementation today.

---

# 8. Voting

Voting combines predictions from different models.

For classification:

```text
Logistic Regression → Cat
Decision Tree       → Cat
kNN                 → Dog
          ↓
       Voting
          ↓
         Cat
```

For regression, models can be combined using their predicted numerical values, often through averaging or weighted averaging.

---

# 9. Stacking

Stacking is another powerful ensemble strategy.

Instead of simply voting:

```text
Model 1 ─┐
Model 2 ─┼──→ Final prediction
Model 3 ─┘
```

we can use another model to learn how to combine their predictions:

```text
Model 1 ─┐
Model 2 ─┼──→ Meta Model → Final Prediction
Model 3 ─┘
```

The final model is called a meta-model or meta-learner.

You don't need to master stacking today.

Just understand the architecture.

# 10. The Big Picture

Memorize this structure:

``` text
ENSEMBLE LEARNING
|
├── Bagging
|    └── Random Forest
|
├── Boosting
|    ├── AdaBoost
|    ├── Gradient Boosting
|    ├── XGBoost
|    ├── LightGBM
|    └── CatBoost
|
├── Voting
|
└── Stacking
```

This is your Week 21 mental map.

# 15. What You Just Built

Your architecture is now:

``` text
                    ┌── Logistic Regression ──┐
                    │                         │
Iris Dataset ───────┼── kNN ──────────────────┼──→ Voting
                    │                         │
                    └── Decision Tree ────────┘
                                              ↓
                                        Final prediction
```

This is your first real ensemble model.

# DAY 1 CONCEPT CHECK

Before moving to Day 2, you should be able to answer these without
looking at your notes:

## Q1.

What is ensemble learning?

## Q2.

Why can combining multiple models improve predictions?

## Q3.

What is majority voting?

## Q4.

Why is model diversity important?

## Q5.

What is the basic idea behind bagging?

## Q6.

What is the basic idea behind boosting?

## Q7.

What is the difference between voting and stacking?

## Q8.

Why does Random Forest use multiple Decision Trees?

## Q9.

If five models all make exactly the same mistake, will majority voting
automatically fix the mistake?

## Q10.

What is the difference between:

``` text
Single Decision Tree
```

and

``` text
Random Forest
```

# DAY 1 COMPLETION CRITERIA

Do not mark Day 1 complete merely because you read the material.

You should have:

-   Understood ensemble learning
-   Understood majority voting
-   Understood model diversity
-   Understood Bagging vs Boosting at a conceptual level
-   Understood Voting vs Stacking
-   Implemented manual majority voting
-   Implemented the diversity experiment
-   Built a `VotingClassifier`
-   Created all 4 files
-   Run the Python code successfully
-   Answered the 10 concept-check questions

Today's most important mental model:

``` text
Single model
      ↓
One source of error

Multiple useful + sufficiently diverse models
      ↓
Combine predictions
      ↓
Reduce impact of individual errors
      ↓
More stable / potentially better prediction
```

Day 2 will move from the theory of ensembles into the first major
ensemble algorithm: Random Forest --- how multiple Decision Trees are
constructed, why randomness is introduced, Bootstrap sampling, feature
randomness, and why Random Forest reduces variance.
