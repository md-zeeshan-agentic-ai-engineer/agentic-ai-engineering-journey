# Phase 2 – Week 17

# Day 1 – Why Evaluation Metrics?

Welcome to **Week 17**! In previous weeks, you built machine learning models such as Logistic Regression and kNN. Now, you will learn **how to evaluate whether a model is actually good**.

A model with **99% accuracy is not always a good model.** Today you will understand why.

---

# Learning Objectives

By the end of Day 1, you should be able to:

- Explain what model evaluation is.
- Understand the difference between Training Accuracy and Test Accuracy.
- Explain why Accuracy alone can be misleading.
- Understand the problem of Class Imbalance.

---

# 1. What is Model Evaluation?

After training a machine learning model, we need to answer one question:

> **"How good is my model?"**

Model evaluation is the process of measuring a model's performance using different metrics.

These metrics help us know:

- Is the model making correct predictions?
- Can it generalize to new data?
- Is it reliable enough to use in real life?

---

# 2. Training Accuracy vs Test Accuracy

Suppose you have 1000 emails.

You split them:

- Training Data = 800 emails
- Test Data = 200 emails

The model learns using the training data.

After learning, it predicts labels on the test data.

## Training Accuracy

Performance on the data the model has already seen.

Example:

Training Accuracy = **99%**

---

## Test Accuracy

Performance on completely unseen data.

Example:

Test Accuracy = **90%**

---

## Why are both important?

If

Training Accuracy = **99%**

Test Accuracy = **98%**

Model is learning well.

If

Training Accuracy = **99%**

Test Accuracy = **65%**

The model has memorized the training data instead of learning patterns.

This is called **Overfitting**.

---

# 3. Why Accuracy Alone is Misleading

Accuracy is calculated as:

```text
Accuracy = Correct Predictions / Total Predictions
```

It looks simple, but it can be misleading.

---

## Example: Cancer Detection

Imagine a hospital has:

- 990 Healthy patients
- 10 Cancer patients

Total = **1000 patients**

Now imagine your model predicts:

> "Everyone is Healthy."

Predictions:

- Healthy predicted correctly = 990
- Cancer predicted correctly = 0

Accuracy:

```text
990 / 1000 = 99%
```

The model reports:

> **Accuracy = 99%**

Sounds amazing...

But it failed to detect **every cancer patient**.

A doctor would never use such a model.

This is why **Accuracy alone is not enough.**

---

# 4. What is Class Imbalance?

Sometimes one class appears much more often than the other.

Example:

Spam Detection

| Email Type | Count |
|------------|------:|
| Normal | 950 |
| Spam | 50 |

Most emails are normal.

If a model predicts:

> "Every email is normal"

Accuracy becomes:

```text
950 / 1000 = 95%
```

Looks good.

But it catches **zero spam emails**.

Again, Accuracy is misleading.

---

# Real-Life Examples

## Medical Diagnosis

- Healthy people = Many
- Sick people = Few

Accuracy alone is not enough.

---

## Fraud Detection

- Normal transactions = Millions
- Fraud transactions = Very few

Need better metrics than accuracy.

---

## Spam Detection

- Most emails are normal.
- Spam emails are rare.

Again, accuracy is insufficient.

---

# Why Do We Need More Metrics?

Because accuracy does not tell us:

- How many positive cases were detected?
- How many mistakes were made?
- Which mistakes are more dangerous?

To answer these questions, we use:

- Confusion Matrix
- Precision
- Recall
- F1-Score
- ROC Curve
- AUC Score

These are the topics for the next days of Week 17.

---

# Summary

- Model evaluation measures how well a machine learning model performs.
- Training Accuracy measures performance on training data.
- Test Accuracy measures performance on unseen data.
- High training accuracy but low test accuracy indicates **overfitting**.
- Accuracy can be misleading when data is imbalanced.
- Real-world applications such as cancer detection, fraud detection, and spam filtering require more than just accuracy.

---

# Practice Questions

1. What is model evaluation?
2. What is the difference between Training Accuracy and Test Accuracy?
3. What is overfitting?
4. Why can accuracy be misleading?
5. What is class imbalance?
6. Give one real-world example where accuracy is not enough.

---

# Mini Assignment

**Answer the following in your own words:**

> **A dataset contains 990 healthy patients and 10 cancer patients. A model predicts every patient as healthy and achieves 99% accuracy. Explain why this model is actually poor.**

---