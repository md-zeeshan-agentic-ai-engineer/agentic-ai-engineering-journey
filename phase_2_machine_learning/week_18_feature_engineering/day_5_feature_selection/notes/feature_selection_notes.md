# Phase 2 --- Week 18 --- Day 5

# Feature Selection

## Overview

Today I move from creating and transforming features to deciding which
features are actually worth keeping.

I already covered:

-   Day 1 → Feature Engineering Fundamentals
-   Day 2 → Feature Scaling
-   Day 3 → Categorical Encoding
-   Day 4 → Missing Value Handling
-   Day 5 → Feature Selection (Today)
-   Day 6 → Complete Feature Engineering Pipeline
-   Day 7 → Titanic Mini Project

------------------------------------------------------------------------

# Day 5 Objective

By the end of today, you should be able to answer:

**"Which features should I give to my machine-learning model, and which
should I remove?"**

You will learn four important techniques:

1.  Correlation Matrix
2.  Variance Threshold
3.  SelectKBest
4.  Feature Importance

And most importantly, you will understand when to use each one.

------------------------------------------------------------------------

# 1. What Is Feature Selection?

Suppose your dataset contains:

-   Age
-   Sex
-   Pclass
-   Fare
-   SibSp
-   Parch
-   Cabin
-   Ticket
-   PassengerId
-   Name

Not every column is equally useful.

Some features may:

-   Contain useful information
-   Contain almost no information
-   Duplicate information
-   Contain noise
-   Increase model complexity
-   Cause overfitting
-   Make the model slower

## Feature Selection means:

Selecting the most useful features for a machine-learning model and
removing unnecessary ones.

------------------------------------------------------------------------

# Example

Suppose we start with:

**10 features**

After feature selection:

-   Age
-   Sex
-   Pclass
-   Fare
-   SibSp

We may discover that these 5 features are enough.

So:

**10 features → 5 useful features**

This can make the model:

-   Simpler
-   Faster
-   Easier to interpret
-   Less noisy
-   Sometimes more accurate

------------------------------------------------------------------------

# 2. Feature Selection vs Feature Engineering

This distinction is extremely important.

## Feature Engineering

You create or transform features.

Examples:

    Age → AgeGroup

or

    FamilySize = SibSp + Parch + 1

## Feature Selection

You choose which existing features to keep.

Example:

    Age → KEEP
    Sex → KEEP
    Pclass → KEEP
    PassengerId → REMOVE

Think:

    Feature Engineering = Build better information

    Feature Selection = Keep the best information

------------------------------------------------------------------------

# 3. Why Remove Unnecessary Features?

Imagine your model receives:

-   Age
-   Fare
-   Pclass
-   Sex
-   PassengerId
-   RandomNumber
-   RandomNumber2
-   RandomNumber3

The model does not necessarily benefit from all of them.

Some may contain:

## Noise

A random feature may have no real relationship with the target.

## Redundant Information

Two features may provide almost the same information.

## Low Variance

A feature that is almost identical for every row may provide very little
information.

## Irrelevant Information

Example:

    PassengerId

Usually does not explain whether a passenger survived.

------------------------------------------------------------------------

# 4. Technique #1 — Correlation Matrix

Correlation measures the relationship between numerical variables.

A common correlation coefficient is:

```text
-1 ≤ correlation ≤ +1
```

## Interpretation

| Correlation | Meaning |
|---:|---|
| +1 | Perfect positive relationship |
| +0.8 | Strong positive relationship |
| +0.2 | Weak positive relationship |
| 0 | No linear relationship |
| -0.2 | Weak negative relationship |
| -0.8 | Strong negative relationship |
| -1 | Perfect negative relationship |

## Example

```text
Age ↔ Fare = 0.15
```

Weak relationship.

But:

```text
TotalPrice ↔ Fare = 0.95
```

Very strong relationship.

That might indicate redundancy.

# 5. Correlation With the Target

Suppose our target is:

```text
Survived
```

We can inspect correlations:

```python
df.corr(numeric_only=True)["Survived"].sort_values(ascending=False)
```

You may get something conceptually like:

```text
Survived    1.00
Fare        0.26
Parch       0.08
SibSp      -0.04
Age        -0.08
Pclass     -0.34
```

This gives us an initial idea of which numerical features have relationships with survival.

## Important

Correlation is not proof of importance.

A feature can have low linear correlation and still be useful to a nonlinear model.

So don’t automatically do:

```text
low correlation → delete
```

Use correlation as an exploratory tool.

# 6. Correlation Between Features

This is another important use.

Suppose:

```text
Feature A ↔ Feature B = 0.98
```

They are extremely correlated.

They may contain nearly duplicate information.

Keeping both may be unnecessary, particularly for some models.

For example:

```text
Height_cm
Height_m
```

are basically the same information.

You don’t need both.


## 7. Visualizing a Correlation Matrix

The heatmap makes strong relationships easier to identify.

## Remember

Correlation mainly measures linear relationships.

It does not detect every possible relationship.