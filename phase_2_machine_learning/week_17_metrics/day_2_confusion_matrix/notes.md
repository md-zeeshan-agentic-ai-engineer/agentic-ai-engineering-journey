# Confusion Matrix

## What is a Confusion Matrix?

A Confusion Matrix is a table used to evaluate the performance of a classification model.

It tells us:

- How many predictions were correct.
- How many predictions were wrong.
- What kind of mistakes the model made.

Instead of only showing one number (accuracy), it provides a complete picture.

---

# Structure of a Confusion Matrix

For binary classification:

| Actual / Predicted | Positive | Negative |
|--------------------|----------|----------|
| Positive           | TP       | FN       |
| Negative           | FP       | TN       |

---

# Four Outcomes

## True Positive (TP)

The model predicted **Positive**, and it was actually **Positive**.

**Example:**

Patient has cancer → Model predicts cancer.

✅ Correct prediction.

---

## True Negative (TN)

The model predicted **Negative**, and it was actually **Negative**.

**Example:**

Healthy patient → Model predicts healthy.

✅ Correct prediction.

---

## False Positive (FP)

The model predicted **Positive**, but it was actually **Negative**.

**Example:**

Healthy patient → Model predicts cancer.

❌ Wrong prediction.

Also called **Type I Error**.

---

## False Negative (FN)

The model predicted **Negative**, but it was actually **Positive**.

**Example:**

Cancer patient → Model predicts healthy.

❌ Wrong prediction.

Also called **Type II Error**.

---

# Example

Suppose we have:

## Actual Labels

- Positive
- Positive
- Negative
- Positive
- Negative
- Negative
- Positive
- Negative

## Predicted Labels

- Positive
- Negative
- Negative
- Positive
- Positive
- Negative
- Positive
- Negative

Let's count:

- TP = 3
- TN = 3
- FP = 1
- FN = 1

### Confusion Matrix

|               | Pred Positive | Pred Negative |
|---------------|---------------|---------------|
| Actual Positive | 3 | 1 |
| Actual Negative | 1 | 3 |

---

# Why is it Useful?

Imagine:

1000 Emails

- 980 Normal
- 20 Spam

If your model predicts:

**"Everything is Normal"**

Accuracy becomes:

98%

Looks amazing...

But the model detected **0 spam emails**.

This is why the Confusion Matrix is important.

---

# Real-Life Examples

## Spam Detection

Positive = Spam

Negative = Normal Email

- TP → Spam correctly detected.
- FP → Normal email marked as spam.
- FN → Spam missed.
- TN → Normal email correctly identified.

---

## Disease Detection

Positive = Disease

Negative = Healthy

- TP → Sick patient correctly diagnosed.
- FP → Healthy patient wrongly diagnosed as sick.
- FN → Sick patient wrongly declared healthy (most dangerous).
- TN → Healthy patient correctly identified.

---

# Summary

- TP = Correct Positive Prediction
- TN = Correct Negative Prediction
- FP = Incorrect Positive Prediction
- FN = Incorrect Negative Prediction

A Confusion Matrix helps us understand not only how many predictions are correct but also what kinds of mistakes a classification model makes.