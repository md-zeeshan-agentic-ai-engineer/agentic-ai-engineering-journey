# DAY 7 — ENSEMBLE DEMO PROJECT

## 🏆 Project: Ensemble Model Comparison

Build a small but proper experiment.

## Compare:

1. Decision Tree
2. Random Forest
3. AdaBoost
4. Gradient Boosting

Use the same dataset and same train/test split.

## Pipeline

Dataset
↓
Cleaning
↓
Train/Test Split
↓
Baseline Decision Tree
↓
Random Forest
↓
AdaBoost
↓
Gradient Boosting
↓
Evaluation
↓
Comparison
↓
Analysis

## 📊 FINAL COMPARISON TABLE

Create something like:

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Decision Tree | — | — | — | — |
| Random Forest | — | — | — | — |
| AdaBoost | — | — | — | — |
| Gradient Boosting | — | — | — | — |

Don't treat the highest number as automatically “the best model.” Analyze the metric relevant to the problem and the trade-offs involved.

# Phase 2 — Week 21 — Day 7

## Ensemble Methods: Ensemble Model Comparison Project

**Language:** English only  
**Phase:** 2 — Machine Learning  
**Week:** 21 — Ensemble Methods  
**Day:** 7 — Final Project & Evaluation  
**Project:** Ensemble Model Comparison  

**Core objective:** Build a reproducible machine learning experiment that compares four classification algorithms, evaluates their performance, and explains the trade-offs between them.

---

## 1. Today's Mission 🎯

Today, you will build a small but professional machine learning experiment.

You will compare these four models:

1. Decision Tree
2. Random Forest
3. AdaBoost
4. Gradient Boosting

You must use **the same dataset, the same train/test split, and the same evaluation metrics** for all four models.

By the end of today, you should be able to answer:

- Which model performs best on the selected dataset?
- Which model generalizes better to unseen data?
- How do accuracy, precision, recall, and F1-score differ?
- Why might a more complex ensemble model perform worse than a simpler model?
- How can you justify your model selection using experimental evidence?

**Important:** Do not assume that the model with the highest accuracy is automatically the best model.

---

## 3. Step 1 — Select the Dataset

Use the **Breast Cancer Wisconsin Diagnostic dataset** included with scikit-learn.

This is a binary classification dataset suitable for comparing the four algorithms.

The target classes are:

- `0`: Malignant
- `1`: Benign

The dataset is useful for learning model comparison because it contains numerical features and a clearly defined classification target.

You do not need to download a separate CSV file.

Create `data/README.md` and add:

```markdown
# Dataset Information

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Source: scikit-learn built-in dataset loader

Task: Binary classification

Target classes:
- 0: Malignant
- 1: Benign

Features: Numerical measurements computed from digitized
images of breast mass samples.

Purpose: Educational machine learning model comparison.

The dataset is loaded directly through scikit-learn.
No external dataset file is required.
```

### Important methodological rule

Because this dataset has a medical context, today's project is for educational experimentation only. It is **not a diagnostic system** and must not be used to make medical decisions.

# Phase 2 — Week 21 Notes

## Why Is Precision and Recall Calculated with `pos_label=0`?

In this dataset, class `0` represents malignant cases.

Therefore, this experiment explicitly treats malignant cases as the positive class when calculating precision, recall, and F1-score.

This helps you examine:

- **Precision:** Among cases predicted as malignant, how many were actually malignant?
- **Recall:** Among all actual malignant cases, how many did the model identify?
- **F1-score:** What is the harmonic mean of precision and recall?

This convention is important because the default positive class in scikit-learn's binary classification metrics is usually `1`.

---

## 6. Step 4 — Analyze the Results

Your final comparison table should follow this format:

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Decision Tree | Actual result | Actual result | Actual result | Actual result |
| Random Forest | Actual result | Actual result | Actual result | Actual result |
| AdaBoost | Actual result | Actual result | Actual result | Actual result |
| Gradient Boosting | Actual result | Actual result | Actual result | Actual result |

Replace the placeholders with values from your actual experiment.

### Analysis Questions

Answer all six questions in your notebook.

**Question 1: Which model achieved the highest accuracy?**

Identify the model and report its measured accuracy.

**Question 2: Which model achieved the highest recall for malignant cases?**

Explain why recall is important when identifying malignant cases.

**Question 3: Which model achieved the highest F1-score?**

Explain what the F1-score tells you about the model's precision and recall.

**Question 4: Did the most accurate model also achieve the highest recall?**

Use your experimental results to support your answer.

**Question 5: Why might Random Forest outperform a single Decision Tree?**

Discuss variance reduction, bootstrap sampling, and combining multiple trees.

**Question 6: Why might a boosting model outperform or underperform Random Forest?**

Discuss sequential learning, error correction, model complexity, and sensitivity to noise.

Do not answer these questions by guessing which model should win. Use your results.

---

## 7. Step 5 — Understand the Main Trade-offs

Use the following table as a conceptual reference.

| Model | Main idea | Potential advantage | Potential limitation |
|---|---|---|---|
| Decision Tree | Learns a hierarchy of decision rules | Interpretable and relatively simple | Can overfit |
| Random Forest | Combines many randomized decision trees | Often reduces variance and improves generalization | Less interpretable than a single tree |
| AdaBoost | Sequentially emphasizes previously misclassified training examples | Can improve a weak learner through boosting | Can be sensitive to noisy or difficult examples |
| Gradient Boosting | Sequentially adds learners to improve an objective | Can model complex relationships effectively | Requires careful tuning and may overfit |

Remember that these are general tendencies, not guaranteed outcomes.

The performance of each algorithm depends on the dataset, hyperparameters, validation strategy, and evaluation metric.

------------------------------------------------------------
# Phase 2 — Week 21 Notes

## Why Is Precision and Recall Calculated with `pos_label=0`?

In this dataset, class `0` represents malignant cases.

Therefore, this experiment explicitly treats malignant cases as the positive class when calculating precision, recall, and F1-score.

This helps you examine:

- **Precision:** Among cases predicted as malignant, how many were actually malignant?
- **Recall:** Among all actual malignant cases, how many did the model identify?
- **F1-score:** What is the harmonic mean of precision and recall?

This convention is important because the default positive class in scikit-learn's binary classification metrics is usually `1`.

---

## 6. Step 4 — Analyze the Results

Your final comparison table should follow this format:

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Decision Tree | Actual result | Actual result | Actual result | Actual result |
| Random Forest | Actual result | Actual result | Actual result | Actual result |
| AdaBoost | Actual result | Actual result | Actual result | Actual result |
| Gradient Boosting | Actual result | Actual result | Actual result | Actual result |

Replace the placeholders with values from your actual experiment.

### Analysis Questions

Answer all six questions in your notebook.

**Question 1: Which model achieved the highest accuracy?**

Identify the model and report its measured accuracy.

**Question 2: Which model achieved the highest recall for malignant cases?**

Explain why recall is important when identifying malignant cases.

**Question 3: Which model achieved the highest F1-score?**

Explain what the F1-score tells you about the model's precision and recall.

**Question 4: Did the most accurate model also achieve the highest recall?**

Use your experimental results to support your answer.

**Question 5: Why might Random Forest outperform a single Decision Tree?**

Discuss variance reduction, bootstrap sampling, and combining multiple trees.

**Question 6: Why might a boosting model outperform or underperform Random Forest?**

Discuss sequential learning, error correction, model complexity, and sensitivity to noise.

Do not answer these questions by guessing which model should win. Use your results.

---

## 7. Step 5 — Understand the Main Trade-offs

Use the following table as a conceptual reference.

| Model | Main idea | Potential advantage | Potential limitation |
|---|---|---|---|
| Decision Tree | Learns a hierarchy of decision rules | Interpretable and relatively simple | Can overfit |
| Random Forest | Combines many randomized decision trees | Often reduces variance and improves generalization | Less interpretable than a single tree |
| AdaBoost | Sequentially emphasizes previously misclassified training examples | Can improve a weak learner through boosting | Can be sensitive to noisy or difficult examples |
| Gradient Boosting | Sequentially adds learners to improve an objective | Can model complex relationships effectively | Requires careful tuning and may overfit |

Remember that these are general tendencies, not guaranteed outcomes.

The performance of each algorithm depends on the dataset, hyperparameters, validation strategy, and evaluation metric.
