# PHASE 2 --- WEEK 18 --- DAY 6

## Complete Feature Engineering Pipeline

You have already covered:

-   Day 1: Introduction to Feature Engineering
-   Day 2: Feature Scaling
-   Day 3: Categorical Encoding
-   Day 4: Missing Value Handling
-   Day 5: Feature Selection

Today we combine all of them into one professional preprocessing
pipeline.

------------------------------------------------------------------------

# DAY 6 --- COMPLETE FEATURE ENGINEERING PIPELINE

## Today's Goal

Build a preprocessing system that can automatically handle:

**Missing Values → Encoding → Scaling → Feature Selection**

using Scikit-learn.

This is an important step toward writing real-world ML code.

------------------------------------------------------------------------

## 1. Why Do We Need a Pipeline?

Imagine a dataset containing:

    Age    Fare Sex      Embarked
  ----- ------- -------- ----------
     22    7.25 male     S
     38   71.28 female   C
    NaN    8.05 female   S
     35     NaN male     Q

A model cannot directly work with:

-   NaN
-   `"male"`
-   `"female"`
-   `"S"`
-   `"C"`
-   `"Q"`

So we need preprocessing.

Normally we could manually do:

``` text
1. Fill missing values
2. Encode categories
3. Scale numbers
4. Select features
5. Train model
```

But manually performing these steps creates problems.

## Pipeline approach

``` text
Raw Dataset
    ↓
Missing Value Handling
    ↓
Categorical Encoding
    ↓
Numerical Scaling
    ↓
Feature Selection
    ↓
ML Model
```

The entire process becomes reproducible.


## 2. The Most Important Concept
Pipeline

A Scikit-learn Pipeline chains preprocessing and modeling steps together.

Basic structure:

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("step1", transformer1),
    ("step2", transformer2),
    ("model", model)
])


For example:

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

#### You don't manually scale X_test.

#### The pipeline does it correctly.

## 3. Why ColumnTransformer?

Our dataset contains different types of columns.

### Numerical columns

- Age
- Fare
- SibSp
- Parch

**Need:**

- Missing value imputation
- Scaling

### Categorical columns

- Sex
- Embarked

**Need:**

- Missing value imputation
- One-hot encoding

We therefore need to apply different preprocessing to different columns.

That's exactly what ColumnTransformer is designed for.

## 15. Understand the Architecture

This single object:

model_pipeline

contains the whole workflow:

                    model_pipeline
                          │
                ┌─────────┴─────────┐
                │                   │
          preprocessor           model
                │                   │
        ┌───────┴───────┐      Logistic
        │               │      Regression
       num             cat
        │               │
   ┌────┴────┐     ┌────┴────┐
   │         │     │         │
Imputer   Scaler Imputer  Encoder

This is the key concept for Day 6.


## ⚠️ 16. Data Leakage

This is extremely important.

❌ Wrong
scaler.fit_transform(X)

before train-test splitting.

Why?

Because information from the test dataset can influence preprocessing.

✅ Correct
pipeline.fit(X_train, y_train)

The preprocessing learns only from training data.

Then:

pipeline.predict(X_test)

uses the already learned transformations.

This is one of the major reasons professional ML workflows use pipelines.


# 17. Where Does Feature Selection Fit?

Your Week 18 roadmap also includes Feature Selection.

Feature selection can be inserted into the pipeline.

For example:

from sklearn.feature_selection import SelectKBest, chi2

However, there is an important issue:

chi2 requires non-negative features, while StandardScaler can produce negative values.

So don't blindly put:

StandardScaler → chi2

together.

This is exactly why understanding each preprocessing step matters.

For today's main pipeline, focus on:

Imputation → Encoding → Scaling → Model

Then we can build a more advanced feature-selection pipeline correctly.

## Key Principle

Fit preprocessing only on training data.

# Pipeline Structure

Raw Data
   ↓
Train/Test Split
   ↓
ColumnTransformer
   ├── Numerical
   │      ↓
   │   Imputation
   │      ↓
   │   Scaling
   │
   └── Categorical
          ↓
       Imputation
          ↓
       Encoding
   ↓
ML Model
   ↓
Prediction
   ↓
Evaluation


# 🎯 DAY 6 SUCCESS CHECKLIST

Before marking Day 6 complete, you should be able to explain:

 What is a Pipeline?
 Why use ColumnTransformer?
 Why do numerical and categorical columns need different preprocessing?
 What does SimpleImputer do?
 Why use median for numerical missing values?
 Why use most-frequent for categorical values?
 What does StandardScaler do?
 What does OneHotEncoder do?
 What is handle_unknown="ignore"?
 What is data leakage?
 Why should preprocessing be fitted only on training data?
 How does preprocessing connect to an ML model?


 # 🏆 Today's Main Takeaway

Earlier, you learned each technique separately:

Day 2 → Scaling
Day 3 → Encoding
Day 4 → Missing Values
Day 5 → Feature Selection

Today you learned how they become a single reproducible ML workflow:

              FEATURE ENGINEERING
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
     Numerical                 Categorical
          ↓                       ↓
      Imputation              Imputation
          ↓                       ↓
       Scaling                Encoding
          └───────────┬───────────┘
                      ↓
                 Preprocessor
                      ↓
                  ML Model
                      ↓
                  Prediction

This is the bridge from learning individual ML techniques to building production-style ML workflows.