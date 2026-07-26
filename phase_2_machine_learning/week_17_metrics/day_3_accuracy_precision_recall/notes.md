# Accuracy, Precision & Recall

## Goal of Today

By the end of today, you will be able to:

- Understand Accuracy, Precision, and Recall.
- Calculate all three metrics manually.
- Know when Accuracy is misleading.
- Understand when Precision is more important than Recall and vice versa.
- Implement these metrics in Python using Scikit-learn.

---

# 1. Why Do We Need These Metrics?

A machine learning model should not only make predictions—it should make good predictions.

Different applications need different evaluation metrics.

Examples:

- Spam Detection
- Cancer Detection
- Fraud Detection
- Face Recognition

Using only Accuracy can sometimes give the wrong impression.

---

# 2. Accuracy

## Definition

Accuracy tells us:

> Out of all predictions, how many were correct?

## Formula

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

## Example

Suppose:

```text
TP = 45
TN = 40
FP = 10
FN = 5
```

Total:

```text
100 samples
```

Accuracy:

```text
Accuracy = (45 + 40) / 100

Accuracy = 85%
```

The model is correct 85% of the time.

---

# 3. Precision

## Definition

Precision answers:

> Out of everything predicted as Positive, how many were actually Positive?

## Formula

```text
Precision = TP / (TP + FP)
```

## Example

Suppose

```text
TP = 80

FP = 20
```

Then

```text
Precision = 80 / (80 + 20)

Precision = 80%
```

Meaning:

Among everything predicted Positive,

80% were actually Positive.

---

# 4. Recall

## Definition

Recall answers:

> Out of all actual Positive cases, how many did we successfully detect?

## Formula

```text
Recall = TP / (TP + FN)
```

## Example

Suppose

```text
TP = 90

FN = 10
```

Then

```text
Recall = 90 / (90 + 10)

Recall = 90%
```

Meaning:

The model found 90% of all real positive cases.

---

# 5. Understanding the Difference

Imagine a hospital.

There are:

```text
100 Cancer Patients
```

Your model detects

```text
90 patients

Misses 10
```

Recall:

```text
90%
```

Now suppose

The model says

```text
100 people have cancer

But only 80 actually have cancer.
```

Then

```text
Precision = 80%
```

---

# 6. When Accuracy Fails

Imagine:

```text
990 Healthy

10 Cancer
```

Total:

```text
1000 people
```

Model predicts:

```text
Everyone is Healthy
```

Accuracy:

```text
990 / 1000

99%
```

Looks amazing.

But...

It detected

```text
0 cancer patients
```

Recall:

```text
0%
```

Precision:

Undefined (no positive predictions)

This is why Accuracy alone is not enough, especially for imbalanced datasets.

---

# 7. When Precision Matters

Precision is important when False Positives are costly.

Examples:

- Spam Detection
- Email Filtering
- Recommendation Systems

Example:

If a real email is marked as spam,

the user may miss an important message.

So we want high Precision.

---

# 8. When Recall Matters

Recall is important when False Negatives are dangerous.

Examples:

- Cancer Detection
- Disease Diagnosis
- Fraud Detection
- Fire Alarm Systems

If a cancer patient is predicted as healthy,

the consequences can be severe.

So we want high Recall.