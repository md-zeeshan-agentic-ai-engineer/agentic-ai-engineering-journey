# 📅 DAY 2 — Bagging

## Bagging = Bootstrap Aggregating

The basic idea:

```text
Original Dataset
        ↓
Bootstrap Sample 1 → Model 1
Bootstrap Sample 2 → Model 2
Bootstrap Sample 3 → Model 3
Bootstrap Sample 4 → Model 4
        ↓
Combine predictions
```

Each model gets a slightly different training sample.

### For classification:

```text
Majority vote
```

### For regression:

```text
Average predictions
```

## Important concept

**Bootstrap sampling** means sampling observations **with replacement**.

### Example:

**Original:**

```text
A B C D E
```

**Possible bootstrap sample:**

```text
A C C D E
```

**Another:**

```text
B B C E E
```

Notice that some observations appear multiple times while some may be absent.
------------------------------------

# Phase 2 — Machine Learning

## Week 21 — Ensembles

### Day 2 — Bagging

You are now on **Week 21, Day 2** of your roadmap.

Yesterday you learned the basic idea of **Ensemble Learning**. Today we go deeper into **Bagging**, because it is the foundation behind **Random Forest**.

---

# DAY 2 OBJECTIVE

By the end of today, you should understand:

1. What Bagging means
2. What Bootstrap Sampling means
3. Why sampling is done with replacement
4. How multiple models are trained
5. How predictions are combined
6. Classification vs Regression in Bagging
7. Why Bagging reduces variance
8. The relationship:

**Bagging → Random Forest**

---

## 1. What is Bagging?

**Bagging = Bootstrap Aggregating**

### The basic idea:

```text
Original Dataset
       ↓
Bootstrap Sample 1 → Model 1
Bootstrap Sample 2 → Model 2
Bootstrap Sample 3 → Model 3
Bootstrap Sample 4 → Model 4
       ↓
Combine Predictions
       ↓
Final Prediction
```

Instead of relying on one model, we train many models on slightly different versions of the training data.

The models then work together.

---

## 2. What is Bootstrap Sampling?

This is one of the most important concepts today.

Suppose our dataset is:

```text
A B C D E
```

A bootstrap sample is created by randomly selecting observations **with replacement**.

For example:

```text
A C C D E
```

### Notice:

- C appears twice
- B does not appear
- The sample still contains 5 observations

Another bootstrap sample could be:

```text
B B C E E
```

Another:

```text
A A B D E
```

So every model receives a slightly different training dataset.

---

## 3. What Does "With Replacement" Mean?

Suppose we randomly select:

```text
A
```

After selecting A, we **put A back into the population**.

So A can be selected again.

### Example:

Original:

```text
A B C D E
```

Selection 1:

```text
C
```

Put C back.

Selection 2:

```text
C
```

Put C back.

Selection 3:

```text
A
```

Selection 4:

```text
D
```

Selection 5:

```text
E
```

Result:

```text
C C A D E
```

That is bootstrap sampling.

### Remember:

**Bootstrap sampling = random sampling with replacement.**

This sentence should become automatic for you.

---

## 4. Why Do We Need Multiple Samples?

Imagine we train one Decision Tree.

A Decision Tree can be sensitive to the training data.

A small change in the dataset can produce a significantly different tree.

This means:

```text
Decision Tree → relatively high variance
```

Bagging attacks this problem.

Instead of:

```text
Dataset → One Tree
```

we create:

```text
Dataset
   ↓
Sample 1 → Tree 1
Sample 2 → Tree 2
Sample 3 → Tree 3
Sample 4 → Tree 4
Sample 5 → Tree 5
   ↓
Combine
```

The individual trees may make different mistakes.

But when their predictions are combined, the overall model can become more stable.

# Bagging — Additional Notes

## 5. Bagging for Classification

Suppose five models predict:

```text
Model 1 → Cat
Model 2 → Dog
Model 3 → Cat
Model 4 → Cat
Model 5 → Dog
```

### Count the votes:

```text
Cat → 3
Dog → 2
```

### Final prediction:

```text
Cat
```

This is called:

**Majority Voting**

```text
Final Class = Most Frequently Predicted Class
```

---

## 6. Bagging for Regression

For regression, we don't use majority voting.

Suppose:

```text
Model 1 → 100
Model 2 → 110
Model 3 → 105
Model 4 → 95
Model 5 → 90
```

The final prediction can be the average:

```text
(100 + 110 + 105 + 95 + 90) / 5
= 100
```

So:

### Classification

```text
Majority Vote
```

### Regression

```text
Average Prediction
```

---

## 7. The Most Important Benefit: Variance Reduction

This is the deeper ML concept.

Bagging is primarily useful for reducing:

**Variance**

Think about a Decision Tree.

A single tree might behave like:

```text
Training Data changes slightly
        ↓
Tree changes significantly
```

With Bagging:

```text
Dataset
   ↓
Tree 1
Tree 2
Tree 3
Tree 4
Tree 5
   ↓
Aggregation
   ↓
More stable prediction
```

Individual models may still be noisy.

But their errors can partially cancel each other.

---

## 8. Bagging vs Boosting

Do not mix these two.

### Bagging

Models are generally trained independently/in parallel.

```text
Dataset
   ↓
Sample 1 → Model 1 ┐
Sample 2 → Model 2 │
Sample 3 → Model 3 ├→ Aggregate
Sample 4 → Model 4 │
Sample 5 → Model 5 ┘
```

### Boosting

Models are trained sequentially.

```text
Model 1
   ↓
Focus on errors
   ↓
Model 2
   ↓
Focus on remaining errors
   ↓
Model 3
   ↓
...
```

### Simple memory trick:

```text
Bagging = many models independently

Boosting = models learn sequentially from previous mistakes
```

---

## 9. Bagging → Random Forest

This connection is extremely important for Week 21.

A Random Forest uses the Bagging idea with Decision Trees.

### Simplified:

```text
Training Dataset
       ↓
Bootstrap Sampling
       ↓
Multiple Decision Trees
       ↓
Random Feature Selection
       ↓
Combine Predictions
       ↓
Random Forest
```

```text
Random Forest
```

So:

> Random Forest is not just "many Decision Trees."

It combines:

1. Bootstrap sampling
2. Multiple Decision Trees
3. Random feature selection
4. Aggregation

We will study this connection more deeply in the next lessons.

# Day 2 — Bagging

## 3. Understand `n_estimators`

This parameter:

```python
n_estimators = 10
```

means:

- Train 10 base models.

### For example:

```text
n_estimators = 1
→ 1 tree

n_estimators = 10
→ 10 trees

n_estimators = 100
→ 100 trees
```

### Try:

```python
n_estimators = 1
```

then:

```python
n_estimators = 50
```

Compare the results.

---

# 🧪 DAY 2 EXPERIMENT

Run the Bagging model with:

```text
n_estimators = 1
n_estimators = 5
n_estimators = 10
n_estimators = 50
n_estimators = 100
```

Create a small table in your notebook:

| n_estimators | Accuracy |
|---:|---:|
| 1 | |
| 5 | |
| 10 | |
| 50 | |
| 100 | |

Do not assume that more trees automatically means better test accuracy.

Your job is to observe what actually happens.

---

# 🧠 DAY 2 CONCEPT CHECK

Answer these **without looking at the notes**:

### Q1.
What does Bagging stand for?

### Q2.
What is bootstrap sampling?

### Q3.
What does “with replacement” mean?

### Q4.
Why can one observation appear multiple times in a bootstrap sample?

### Q5.
How are predictions combined for classification?

### Q6.
How are predictions combined for regression?

### Q7.
What problem does Bagging primarily help reduce?

### Q8.
What is the difference between Bagging and Boosting?

### Q9.
What important technique does Random Forest add to the Bagging + Decision Tree idea?

### Q10.
What does `n_estimators` control?

---

# 🧰 DAY 2 MINI PROJECT

## Build:

### Bagging Classifier Comparison

Use the Iris dataset.

### Compare:

```text
Single Decision Tree

VS

Bagging Classifier
```

### Your output should contain:

```text
Single Decision Tree Accuracy: ___

Bagging Accuracy: ___
```

Then write a short conclusion:

```text
Bagging uses multiple models trained on bootstrap samples
and combines their predictions. Compared with a single
Decision Tree, this can produce a more stable model by
reducing variance.
```

Do not simply copy that conclusion—rewrite it in your own words.

---

# ✅ DAY 2 COMPLETION CRITERIA

Don't mark Day 2 complete until you can explain this entire chain without notes:

```text
Original Dataset
        ↓
Bootstrap Sampling
        ↓
Different Training Samples
        ↓
Multiple Models
        ↓
Predictions
        ↓
Aggregation
        ↓
Final Prediction
```

# Day 2 — Bagging

## 3. Understand `n_estimators`

This parameter:

```python
n_estimators = 10
```

means:

- Train 10 base models.

### For example:

```text
n_estimators = 1
→ 1 tree

n_estimators = 10
→ 10 trees

n_estimators = 100
→ 100 trees
```

### Try:

```python
n_estimators = 1
```

then:

```python
n_estimators = 50
```

Compare the results.

---

# 🧪 DAY 2 EXPERIMENT

Run the Bagging model with:

```text
n_estimators = 1
n_estimators = 5
n_estimators = 10
n_estimators = 50
n_estimators = 100
```

Create a small table in your notebook:

| n_estimators | Accuracy |
|---:|---:|
| 1 | |
| 5 | |
| 10 | |
| 50 | |
| 100 | |

Do not assume that more trees automatically means better test accuracy.

Your job is to observe what actually happens.

---

# 🧠 DAY 2 CONCEPT CHECK

Answer these **without looking at the notes**:

### Q1.
What does Bagging stand for?

### Q2.
What is bootstrap sampling?

### Q3.
What does “with replacement” mean?

### Q4.
Why can one observation appear multiple times in a bootstrap sample?

### Q5.
How are predictions combined for classification?

### Q6.
How are predictions combined for regression?

### Q7.
What problem does Bagging primarily help reduce?

### Q8.
What is the difference between Bagging and Boosting?

### Q9.
What important technique does Random Forest add to the Bagging + Decision Tree idea?

### Q10.
What does `n_estimators` control?

---

# 🧰 DAY 2 MINI PROJECT

## Build:

### Bagging Classifier Comparison

Use the Iris dataset.

### Compare:

```text
Single Decision Tree

VS

Bagging Classifier
```

### Your output should contain:

```text
Single Decision Tree Accuracy: ___

Bagging Accuracy: ___
```

Then write a short conclusion:

```text
Bagging uses multiple models trained on bootstrap samples
and combines their predictions. Compared with a single
Decision Tree, this can produce a more stable model by
reducing variance.
```

Do not simply copy that conclusion—rewrite it in your own words.

---

# ✅ DAY 2 COMPLETION CRITERIA

Don't mark Day 2 complete until you can explain this entire chain without notes:

```text
Original Dataset
        ↓
Bootstrap Sampling
        ↓
Different Training Samples
        ↓
Multiple Models
        ↓
Predictions
        ↓
Aggregation
        ↓
Final Prediction
```


---

# Especially Remember

```text
Bagging
   ↓
Bootstrap Sampling
   ↓
Multiple Models
   ↓
Aggregation
   ↓
Variance Reduction
```

## 🔥 Today's Core Takeaway

Bagging makes many models learn from different bootstrap samples and combines their predictions to obtain a more stable overall model.

## Next

**Week 21 — Day 3 — Random Forest fundamentals and why Random Forest is more powerful than plain Bagging with Decision Trees.**
