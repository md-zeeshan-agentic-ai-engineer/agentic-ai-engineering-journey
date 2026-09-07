# PHASE 2 — WEEK 18 — DAY 4
# Handling Missing Values

Welcome to Day 4 of Week 18: Feature Engineering.

Today we focus on one of the most important data-preprocessing skills in Machine Learning:

> How to detect, understand, and handle missing values correctly.

By the end of today, you should be able to take a dataset containing `NaN` values and prepare it safely for a Machine Learning model.

---

# DAY 4 — LEARNING OBJECTIVES

Today you will learn:

- What missing values are
- Why missing values occur
- How to detect missing values
- How to count missing values
- How to calculate missing-value percentages
- When to drop missing rows
- When to use mean imputation
- When to use median imputation
- When to use mode imputation
- How to use `SimpleImputer`
- How to avoid data leakage during imputation
- How missing-value handling fits into a preprocessing pipeline

---

## 1. What Is a Missing Value?

A missing value means that a particular observation does not contain a value for a feature.

For example:

| Age | Fare | Embarked |
|---:|---:|---|
| 22 | 7.25 | S |
| 38 | 71.28 | C |
| NaN | 8.05 | S |
| 35 | NaN | Q |

Here:

- `Age` has one missing value.
- `Fare` has one missing value.
- `Embarked` has no missing value.

In pandas, missing numerical data is commonly represented as:

```python
NaN

## 2. Why Do Missing Values Happen?

Missing data can occur for many reasons.

## Human Error

A person may forget to enter information.

## Sensor Failure

A sensor may fail to record a measurement.

## Data Collection Problems

Some information may simply not have been collected.

## Privacy

A person may intentionally refuse to provide information.

## Different Data Sources

When combining datasets, some columns may not exist in every source.


## 3. Why Are Missing Values a Problem?

Many Machine Learning algorithms cannot directly work with missing values.

For example:

```text
Age = 25
Age = 31
Age = NaN
Age = 42

A model cannot simply calculate normally with an undefined value.

Therefore, before training:

Raw Data
   ↓
Detect Missing Values
   ↓
Handle Missing Values
   ↓
Clean Dataset
   ↓
Machine Learning Model


## 4. Detect Missing Values

Example:

PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Fare             0
Embarked         2

This immediately tells us where the missing data exists.

## 5. Missing-Value Percentage

Counting missing values is useful.

But percentage is often even more informative.

For example:

Age         19.87
Cabin       77.10
Embarked     0.22

This tells us that approximately:

20% of Age is missing.
77% of Cabin is missing.
Very little Embarked data is missing.

This information helps us decide what to do.


6. Handle Missing Values

Method 1 — Drop Missing Rows

The simplest approach is:

df_clean = df.dropna()

This removes rows containing missing values.

Example:

Before

Age
22
38
NaN
35
40

After dropna()

Age
22
38
35
40
Advantage

Very simple.

Disadvantage

You may throw away valuable data.

If a dataset contains 1,000 rows and 300 rows have missing values, dropping them could leave only 700 rows.

That's a significant loss.

When Should You Drop Rows?

Dropping rows can make sense when:

Only a tiny number of rows contain missing values.
The missing observations are not important.
The dataset is large enough.
Removing the rows will not introduce serious bias.

For example:

1,000,000 rows
5 missing rows

Dropping those five rows is usually not a major problem.

But:

1,000 rows
400 missing rows

Dropping them would be much more serious.

Method 2 — Mean Imputation

Imputation means replacing missing values with an estimated value.

For numerical data, one option is the mean.

Suppose:

Age
20
30
40
NaN
50

Mean:

(20 + 30 + 40 + 50) / 4 = 35

So:

Age
20
30
40
35
50

In pandas:

df["Age"] = df["Age"].fillna(df["Age"].mean())
When Should You Use Mean?

Mean imputation can work well when:

The numerical feature is reasonably symmetric.
There are no extreme outliers.
The mean represents the distribution reasonably well.

However, mean can be strongly affected by outliers.

Example:

20, 21, 22, 23, 200

The value 200 significantly increases the mean.



Method 3 — Median Imputation

The median is often safer when data contains outliers.

Example:

20
21
22
23
200

Sorted:

20, 21, 22, 23, 200

Median:

22

So we could replace:

NaN → 22

In pandas:

df["Age"] = df["Age"].fillna(df["Age"].median())

⭐ Mean vs Median
Situation	Better Choice
Symmetric numerical data	Mean
Data with outliers	Median
Highly skewed data	Usually Median
Income / salary	Often Median
Age	Often Median can be reasonable

A useful rule:

If you are unsure and the numerical feature is skewed or contains outliers, median is often a safer starting point.


Method 4 — Mode Imputation

For categorical features, mean and median do not make sense.

Example:

Sex
male
female
female
NaN
male

The most frequent value is:

female

This is called the mode.

We can use:

df["Sex"] = df["Sex"].fillna(df["Sex"].mode()[0])




Choosing the Right Strategy

A simple decision framework:

                Missing Value
                     │
          ┌──────────┴──────────┐
          │                     │
      Numerical             Categorical
          │                     │
     ┌────┴────┐             Mode
     │         │
  Normal    Skewed/
  data      Outliers
     │         │
    Mean     Median


But remember:

There is no universal imputation strategy.

You should understand the data before choosing.




Why SimpleImputer Is Important

You will eventually build Machine Learning pipelines.

Instead of manually doing:

fillna()

everywhere, we can create preprocessing steps.

For example:

Numerical Features
       ↓
SimpleImputer
       ↓
StandardScaler
       ↓
Model

And:

Categorical Features
       ↓
SimpleImputer
       ↓
OneHotEncoder
       ↓
Model

This becomes extremely useful when we build the complete preprocessing pipeline on Day 6.