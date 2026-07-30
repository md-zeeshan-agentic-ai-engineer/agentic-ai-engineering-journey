# Phase 2 – Week 17 – Day 5

# ROC Curve & AUC

---

# Understand the Problem

Suppose you have built a Spam Detection model.

The model predicts:

- Spam
- Not Spam

Looking at Accuracy alone is not enough.

Why?

Because the model also gives a confidence score (probability).

Example:

| Email | Spam Probability |
|--------|------------------|
| A | 0.98 |
| B | 0.90 |
| C | 0.70 |
| D | 0.55 |
| E | 0.20 |

The question is:

**At what probability should an email be considered Spam?**

This is called the **Threshold**.

---

# 1. Probability Threshold

A Machine Learning model first predicts probabilities before making the final prediction.

Example:

| Probability | Prediction |
|-------------|------------|
| 0.95 | Spam |
| 0.80 | Spam |
| 0.60 | Spam |
| 0.40 | Not Spam |
| 0.10 | Not Spam |

Normally the threshold is

```python
0.5
```

Rule:

```text
Probability >= 0.5

Spam
```

```text
Probability < 0.5

Not Spam
```

---

## What Happens If We Change the Threshold?

### Threshold = 0.8

An email will be classified as Spam only if the probability is greater than or equal to **80%**.

The model becomes very strict.

---

### Threshold = 0.2

The model will classify almost everything as Spam.

False Positives will increase.

---

ROC Curve is created by changing this threshold.

---

# 2. True Positive Rate (TPR)

Another name for TPR is

```text
Recall
```

Formula

```text
TPR = TP / (TP + FN)
```

Meaning

Out of all Actual Positive samples, how many were correctly detected?

Example

There were **100 Spam emails**.

The model detected **90**.

```text
TP = 90

FN = 10
```

TPR

```text
90 / (90 + 10)

= 0.90
```

Means

```text
90%
```

The model detected **90% of Spam emails**.

---

# 3. False Positive Rate (FPR)

Formula

```text
FPR = FP / (FP + TN)
```

Meaning

Out of all Actual Negative samples, how many were incorrectly classified as Positive?

Example

There were **100 Normal emails**.

The model incorrectly predicted **10** as Spam.

```text
FP = 10

TN = 90
```

FPR

```text
10 / (10 + 90)

= 0.10
```

Means

```text
10%
```

The model made **10% false alarms**.

---

# Simple Example

Suppose

```text
TP = 80

FP = 20

TN = 70

FN = 30
```

TPR

```text
80 / (80 + 30)

= 0.727
```

FPR

```text
20 / (20 + 70)

= 0.222
```

This becomes one point on the ROC graph.

---

# 4. ROC Curve

ROC stands for

```text
Receiver Operating Characteristic
```

You do not need to memorize the name.

Understand the concept.

ROC Curve is a graph.

**X-axis**

```text
False Positive Rate (FPR)
```

**Y-axis**

```text
True Positive Rate (TPR)
```

```
TPR ↑

1.0 |           ●
    |        ●
    |      ●
    |    ●
    |  ●
0.0 +-------------------->

      0.0        1.0

           FPR
```

Each point represents a different Threshold.

Threshold changes from

```text
1.0

0.9

0.8

0.7

0.6

...

0.0
```

For every threshold, calculate

```text
TPR

FPR
```

Then plot the graph.

This graph is called the **ROC Curve**.

---

# What Does ROC Curve Tell Us?

It shows how well the model detects Positive samples while minimizing False Positives.

A good model has

```text
High TPR

Low FPR
```

---

# Worst Model

```
|

|      /

|    /

|  /

|/

+-------------
```

This represents **Random Guessing**.

Such a model is not useful.

---

# Perfect Model

```
|

|■■■■■■■■

|       ■

|       ■

+-------------
```

This is the best possible ROC Curve.

---

# 5. AUC

AUC stands for

```text
Area Under Curve
```

It is the total area under the ROC Curve.

---

Example

AUC

```text
1.0
```

Perfect Model

---

AUC

```text
0.9
```

Excellent Model

---

AUC

```text
0.8
```

Very Good Model

---

AUC

```text
0.7
```

Good Model

---

AUC

```text
0.6
```

Poor Model

---

AUC

```text
0.5
```

Random Guess

---

# AUC Interpretation Table

| AUC | Meaning |
|------|---------|
| 1.0 | Perfect |
| 0.9 | Excellent |
| 0.8 | Very Good |
| 0.7 | Good |
| 0.6 | Poor |
| 0.5 | Random Guess |

---

# Real-Life Example

## Hospital Cancer Detection

There are **1000 Patients**.

```text
Cancer = 100

Healthy = 900
```

### Model A

Accuracy

```text
99%
```

But

The model does not detect Cancer at all.

This is a poor model.

---

### Model B

Accuracy

```text
95%
```

The model detects almost all Cancer cases.

ROC Curve is also good.

AUC

```text
0.98
```

Model B is much more useful.

This is why in medical applications, **ROC-AUC is often more important than Accuracy**.

---

# Key Takeaways

### Probability Threshold
- Default threshold is **0.5**.
- Threshold controls the final prediction.

### True Positive Rate (Recall)
- Measures how many actual positive samples are correctly detected.

Formula

```text
TP / (TP + FN)
```

### False Positive Rate
- Measures how many actual negative samples are incorrectly predicted as positive.

Formula

```text
FP / (FP + TN)
```

### ROC Curve
- X-axis = False Positive Rate (FPR)
- Y-axis = True Positive Rate (TPR)
- Every point represents a different Threshold.

### AUC
- Area under the ROC Curve.
- Higher AUC means a better classifier.
- **1.0 = Perfect**
- **0.5 = Random Guess**

---

# Day 5 Learning Outcome

After completing Day 5, you should be able to:

- Explain Probability Threshold.
- Understand how changing the threshold affects predictions.
- Calculate TPR and FPR.
- Explain the ROC Curve.
- Interpret the ROC Curve.
- Understand AUC Score and its significance.
- Implement `roc_curve()` and `roc_auc_score()` using Scikit-learn.
- Plot the ROC Curve using Matplotlib.
- Evaluate a classification model using ROC-AUC.