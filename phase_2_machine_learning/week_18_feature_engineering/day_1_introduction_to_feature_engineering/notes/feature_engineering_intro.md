# Feature Engineering - Day 1 Notes

## What is Feature Engineering?

Feature Engineering is the process of creating, transforming, selecting, and preparing input variables (features) so that Machine Learning models can learn patterns more effectively.

A feature is simply an input variable (column) in a dataset.

Example:

| Age | Salary | City | Purchased |
|-----|--------|------|-----------|
| 25 | 40000 | Delhi | Yes |

Features:
- Age
- Salary
- City

Target:
- Purchased

---

## Why is Feature Engineering Important?

Machine Learning algorithms learn from features, not raw data.

Good features lead to:
- Higher accuracy
- Faster training
- Better predictions
- Less overfitting
- Easier interpretation

Example:

Birth Year = 1999

Create:

Age = Current Year - Birth Year

Age is much more useful for prediction.

---

## Why Feature Engineering Improves Model Performance

Suppose you want to predict house prices.

Raw Data:

Length = 20 m

Width = 15 m

Instead of giving only Length and Width, create a new feature:

Area = Length × Width

The model understands property size much better.

Feature Engineering helps models discover useful patterns.

Another Example:

Hours Studied = 6

Attendance = 90%

Create:

Study Efficiency = Hours Studied × Attendance

This new feature may improve prediction performance.

---

# Types of Features

Machine Learning datasets usually contain four main feature types.

## 1. Numerical Features

Contain numbers.

Examples:
- Age
- Salary
- Height
- Weight
- Temperature

Example:

| Age | Salary |
|-----|--------|
|22|25000|
|35|50000|

These features support mathematical operations.

---

## 2. Categorical Features

Contain categories or names.

Examples:
- City
- Country
- Color
- Department

Example:

| City |
|------|
| Delhi |
| Mumbai |
| Kolkata |

Most Machine Learning algorithms cannot directly use categorical features.

They must first be converted into numbers using Encoding.

---

## 3. Ordinal Features

Contain categories that have a meaningful order.

Examples:

Education Level:
- High School
- Bachelor
- Master
- PhD

Customer Rating:
- Poor
- Average
- Good
- Excellent

Order matters.

---

## 4. Binary Features

Contain only two possible values.

Examples:
- Yes / No
- True / False
- 0 / 1
- Male / Female

Example:

| Purchased |
|-----------|
| Yes |
| No |

Binary features are usually easy to convert into numbers.

---

# Summary Table

| Feature Type | Example |
|--------------|---------|
| Numerical | Age, Salary |
| Categorical | City, Country |
| Ordinal | Education Level |
| Binary | Yes / No |

---

# Titanic Dataset Feature Types

| Column | Feature Type |
|---------|--------------|
| PassengerId | Numerical |
| Survived | Binary |
| Pclass | Ordinal |
| Name | Categorical |
| Sex | Binary |
| Age | Numerical |
| SibSp | Numerical |
| Parch | Numerical |
| Fare | Numerical |
| Embarked | Categorical |

---

# Key Takeaways

- A feature is an input variable.
- Feature Engineering prepares data so Machine Learning models learn better.
- Better features often improve accuracy more than changing algorithms.
- The four common feature types are:
  - Numerical
  - Categorical
  - Ordinal
  - Binary
- Identifying feature types is the first step in data preprocessing.