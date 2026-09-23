# PHASE 2 — MACHINE LEARNING

## WEEK 20 — TREES

### DAY 4 — Build Your First Decision Tree 🌳

**Language: Fully English**

You are now at Week 20, Day 4.

Your Week 20 target is:

- **Core Focus:** Decision Trees
- **Skill Output:** Build, evaluate, and reason about Decision Tree models
- **Project Output:** Tree Model

Today we move from understanding the algorithm — actually building and experimenting with it.

---

## 🎯 DAY 4 OBJECTIVE

By the end of today, you should be able to:

- Build a `DecisionTreeClassifier`
- Train it using `.fit()`
- Make predictions using `.predict()`
- Evaluate accuracy
- Understand `max_depth`
- Compare training vs testing performance
- Recognize underfitting vs overfitting
- Explain why tree depth matters

**The most important mindset:**

> Do not just learn how to call Scikit-learn. Learn what the algorithm is doing and why its performance changes.

---

## 5. Understand What Just Happened

Think of tree depth as the model's ability to keep making decisions.

### Shallow tree

```text
Depth = 1
```

Very simple decision rules.

It may fail to capture important patterns.

**Potential underfitting**

---

### Medium tree

```text
Depth = 3–5
```

More complex decisions.

It may capture useful patterns without becoming excessively specialized.

---

### Very deep tree

```text
Depth = 10+
```

The tree can keep splitting the data into increasingly specific groups.

It may eventually memorize the training data.

**Potential overfitting**

---

## 6. Your Mental Model

Remember this:

```text
Low complexity
      ↓
Underfitting
      ↓
Increasing complexity
      ↓
Better generalization
      ↓
Too much complexity
      ↓
Overfitting
```

The goal is not:

> "Get 100% training accuracy."

The goal is:

> Learn patterns that generalize to unseen data.

This is one of the most important ideas in machine learning.

---

## 7. DAY 4 EXPERIMENT

Create a table in your notebook:

| max_depth | Training Accuracy | Test Accuracy | Observation |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 5 | | | |
| 10 | | | |

Fill it using your experiment.

Then answer these questions:

### Q1

Which depth produced the highest training accuracy?

### Q2

Which depth produced the highest test accuracy?

### Q3

At what depth did the model begin showing signs of overfitting?

### Q4

What happens to training accuracy as tree depth increases?

### Q5

Does test accuracy always increase when model complexity increases?

**Do not guess. Use your experimental results.**

---

## 8. Important Concept: Generalization

Today's most important concept is:

### Generalization

A model is useful when it performs well on data it has never seen before.

Think:

```text
Training Data
      ↓
Learn patterns
      ↓
Model
      ↓
Unseen Test Data
      ↓
Generalization
```

A model that memorizes training examples but performs badly on unseen examples is not a strong ML model.

---

## 🔴 DAY 4 — ENGINEER THINKING

### Do not memorize:

```python
DecisionTreeClassifier()
```

Instead, understand:

```text
Data
  ↓
Possible split
  ↓
Does the split improve the separation?
  ↓
Choose a useful split
  ↓
Split data
  ↓
Repeat
  ↓
Stop according to constraints
  ↓
Prediction
```

This is the bridge between:

> "I know Scikit-learn"

and

> "I understand machine learning algorithms."


---

## ✅ DAY 4 COMPLETION CHECKLIST

Before marking Day 4 complete, you should be able to check all of these:

- [ ] I built a Decision Tree classifier.
- [ ] I trained it with `.fit()`.
- [ ] I generated predictions with `.predict()`.
- [ ] I calculated training accuracy.
- [ ] I calculated test accuracy.
- [ ] I experimented with `max_depth`.
- [ ] I understand underfitting.
- [ ] I understand overfitting.
- [ ] I understand why training and test performance can differ.
- [ ] I understand why generalization matters.
- [ ] I completed the depth experiment.
- [ ] I can explain what a Decision Tree is doing without relying only on Scikit-learn terminology.

---

## 🏆 DAY 4 SUCCESS CONDITION

Don't mark Day 4 complete just because the code ran.

Mark it complete when you can explain this sentence in your own words:

> "Increasing the complexity of a Decision Tree can improve its ability to fit training data, but excessive complexity can hurt its ability to generalize to unseen data."

**Next: Day 5 — Decision Tree Hyperparameters + Overfitting Control.**
