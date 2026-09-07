# PHASE 2 — WEEK 18 — DAY 7

## Mini Project: Titanic Survival Prediction — Feature Engineering Focus

Today is the final day of Week 18. The goal is not to learn a completely new ML algorithm; it is to combine everything from Days 1–6 into one clean, reproducible feature-engineering workflow.

---

# Day 7 Objective

By the end of today, you should be able to take a raw Titanic dataset and:

**Raw Data → Clean → Handle Missing Values → Engineer Features → Encode → Scale → Select Features → Save Processed Dataset**

Your final deliverables will be:

processed_titanic.csv
feature_engineering.ipynb
README.md

# 1. Project Problem

## Business/ML Question

> Can we prepare the Titanic dataset into a high-quality machine-learning-ready dataset for predicting passenger survival?

---

## Target Variable

Our target variable is:

Survived

Where:

0 = Did not survive
1 = Survived

Important:

Today we are primarily building the preprocessing/feature-engineering pipeline.

We are not focusing on achieving the highest possible model accuracy yet.

# 2. Titanic Features

The classic Titanic dataset contains columns such as:

| Feature     | Type             | Meaning                 |
| ----------- | ---------------- | ----------------------- |
| PassengerId | Numerical        | Passenger identifier    |
| Survived    | Binary           | Target                  |
| Pclass      | Ordinal          | Passenger class         |
| Name        | Categorical/Text | Passenger name          |
| Sex         | Categorical      | Gender                  |
| Age         | Numerical        | Passenger age           |
| SibSp       | Numerical        | Siblings/spouses aboard |
| Parch       | Numerical        | Parents/children aboard |
| Ticket      | Categorical/Text | Ticket number           |
| Fare        | Numerical        | Ticket fare             |
| Cabin       | Categorical      | Cabin                   |
| Embarked    | Categorical      | Port of embarkation     |


# 🏆 Week 18 Completion Checklist

Before marking Week 18 complete, you should be able to explain these without looking at notes:

 What is feature engineering?
 Why do we scale features?
 StandardScaler vs MinMaxScaler
 RobustScaler
 Label Encoding
 One-Hot Encoding
 Ordinal Encoding
 Missing-value detection
 Mean vs median vs mode imputation
 SimpleImputer
 Feature selection
 Correlation
 Variance Threshold
 SelectKBest
 Feature importance
 Pipeline
 ColumnTransformer
 Train/test split
 Data leakage
 fit_transform() vs transform()



# The Most Important Lesson of Day 7

The real skill you're building is not memorizing individual preprocessing functions.

It is learning to think like an ML engineer:

RAW DATA
   ↓
UNDERSTAND
   ↓
CLEAN
   ↓
HANDLE MISSING VALUES
   ↓
ENGINEER / TRANSFORM FEATURES
   ↓
ENCODE
   ↓
SCALE
   ↓
SELECT
   ↓
PIPELINE
   ↓
ML-READY DATA

This is the bridge between basic machine learning and production-quality ML workflows.