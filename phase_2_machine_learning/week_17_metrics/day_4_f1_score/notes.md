# F1-Score

---

# Learn

Understand:

- Harmonic Mean of Precision and Recall
- Why F1-Score is useful for imbalanced datasets

---

# Formula

\[
F1 = \frac{2 \times Precision \times Recall}{Precision + Recall}
\]

or

```text
F1 = 2 × (Precision × Recall)
     -------------------------
      Precision + Recall
```

---

# Why do we need F1 Score?

Accuracy can be misleading.

Precision only measures:

> "When the model predicts Positive, how often is it correct?"

Recall only measures:

> "How many actual positives did the model find?"

F1 combines both into one metric.

---

# Example

Suppose

```text
Precision = 0.80

Recall = 0.60
```

Then

```text
F1

= 2 × 0.80 × 0.60
  ----------------
   0.80 + 0.60

= 0.96 / 1.40

= 0.686
```

F1 Score = **0.69**

---

# Why Harmonic Mean?

Normal average

```text
(0.8 + 0.6)/2 = 0.7
```

But Harmonic Mean

```text
0.686
```

The harmonic mean penalizes models when either Precision or Recall is low.

So a model must perform well on both.