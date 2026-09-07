# Phase 2 — Week 18 — Day 3

# Encoding Categorical Features

Welcome to Day 3 of Feature Engineering! Yesterday you learned Feature Scaling. Today you'll learn how to convert categorical data into numerical data, because machine learning algorithms work with numbers, not text.

---

# Learning Objectives

By the end of today, you will be able to:

- Understand what categorical features are.
- Know the difference between:
  - Label Encoding
  - One-Hot Encoding
  - Ordinal Encoding
- Choose the correct encoding technique.
- Encode categorical columns using Scikit-learn.
- Apply encoding on the Titanic dataset.

---

# 1. What are Categorical Features?

Categorical features contain **labels or names instead of numbers**.

### Example:

| Passenger | Gender |
|-----------|--------|
| A | Male |
| B | Female |
| C | Male |

Machine learning models cannot understand Male or Female directly.

We must convert them into numbers.

This process is called **Encoding**.

---

# Types of Categorical Variables

## 1. Nominal Features

No natural order exists.

### Example:

- Red
- Blue
- Green

or

- Delhi
- Mumbai
- Kolkata

These categories are simply different.

---

## 2. Ordinal Features

These have an order.

### Example:

Education

**High School < Bachelor's < Master's < PhD**

Another example:

**Small < Medium < Large**

The order matters.

---

# Why Encoding is Necessary

Suppose your dataset contains:

### Color

- Red
- Blue
- Green

A machine learning model only understands numbers.

### After encoding:

| Color |
|-------|
| 0 |
| 1 |
| 2 |

Now the model can process the data.


# Method 1 — Label Encoding

Each category receives an integer.

## Example

### Animal

- Cat
- Dog
- Horse

Each category is converted into an integer value.

For example:

| Animal | Encoded |
|--------|---------|
| Cat | 0 |
| Dog | 1 |
| Horse | 2 |

---

## Advantages

- Very simple
- Fast
- Uses little memory

---

## Disadvantages

The model may assume an order between the encoded values.

For example:

**Horse > Dog > Cat**

This suggests that Horse is greater than Dog and Dog is greater than Cat.

However, this is not true because animals such as Cat, Dog, and Horse are simply different categories.

Therefore, **Label Encoding is not suitable for nominal data.**


# Method 2 — One-Hot Encoding

This is the most commonly used encoding.

Instead of one column, multiple binary columns are created.

## Example

### Original

| Color |
|-------|
| Red |
| Blue |
| Green |

### Encoded

| Red | Blue | Green |
|-----|------|-------|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

No false ordering is introduced.

---

## Advantages

- Best for nominal data
- No artificial ordering
- Improves model performance

---

## Disadvantages

If there are many categories, many new columns are created.

### Example

Country column with 200 countries → 200 new columns.


# Method 3 — Ordinal Encoding

Used only when categories have a meaningful order.

## Example

### Size

- Small
- Medium
- Large

### Encoding

- Small → 0
- Medium → 1
- Large → 2

The order of the categories is meaningful:

**Small < Medium < Large**

---

# Which Encoding Should You Use?

| Situation | Best Method |
|-----------|-------------|
| Gender | Label Encoding (binary) |
| City | One-Hot Encoding |
| Country | One-Hot Encoding |
| Education Level | Ordinal Encoding |
| T-Shirt Size | Ordinal Encoding |
| Colors | One-Hot Encoding |


# Titanic Dataset Practice

## Encoding Titanic Dataset Columns

Titanic dataset mein different columns ke liye different encoding approaches use kiye ja sakte hain.

| Column | Encoding |
|---|---|
| Sex | Label Encoding (or binary mapping) |
| Embarked | One-Hot Encoding |
| Pclass | Keep as ordinal/integer |
| Survived | Target variable (no encoding needed) |

## Practice Exercise

- Encode the Sex column using LabelEncoder.
- Encode the Embarked column using OneHotEncoder.
- Create a dataset with a Size column (Small, Medium, Large) and apply OrdinalEncoder.
- Compare the outputs of all three encoding methods.
- Explain why One-Hot Encoding is preferred over Label Encoding for nominal data.

---

## 1. Sex

**Encoding Method:** Label Encoding (or binary mapping)

The `Sex` column contains two categories:

- Male
- Female

Since it is a binary categorical feature, Label Encoding or binary mapping can be used.

Example:

- Male → 1
- Female → 0

---

## 2. Embarked

**Encoding Method:** One-Hot Encoding

The `Embarked` column contains multiple nominal categories:

- S
- C
- Q

These categories do not have a meaningful order.

Therefore, One-Hot Encoding is appropriate.

After One-Hot Encoding, the column is converted into separate binary columns:

- `Embarked_C`
- `Embarked_Q`
- `Embarked_S`

Each row has `1` for the category it belongs to and `0` for the other categories.

Example:

| Embarked | Embarked_C | Embarked_Q | Embarked_S |
|---|---:|---:|---:|
| S | 0 | 0 | 1 |
| C | 1 | 0 | 0 |
| Q | 0 | 1 | 0 |

---

## 3. Pclass

**Encoding:** Keep as ordinal/integer

The `Pclass` column represents passenger class:

- 1st Class
- 2nd Class
- 3rd Class

It can be kept as an ordinal/integer feature because the class values already represent an ordered level.

Therefore, additional categorical encoding is not necessary.

---

## 4. Survived

**Encoding:** Target variable (no encoding needed)

The `Survived` column is the target variable in the Titanic prediction problem.

It represents whether a passenger survived:

- `0` → Did not survive
- `1` → Survived

Since it is the target variable, no categorical feature encoding is required.

---

# Summary

| Titanic Column | Type / Meaning | Recommended Approach |
|---|---|---|
| Sex | Binary categorical | Label Encoding / Binary Mapping |
| Embarked | Nominal categorical | One-Hot Encoding |
| Pclass | Ordinal / Integer | Keep as ordinal/integer |
| Survived | Target variable | No encoding needed |

## Key Point

Different categorical columns may require different encoding methods.

- **Binary categories** → Label Encoding / Binary Mapping
- **Nominal categories with no order** → One-Hot Encoding
- **Ordinal categories with meaningful order** → Keep as ordinal values or use Ordinal Encoding
- **Target variable** → No feature encoding is required