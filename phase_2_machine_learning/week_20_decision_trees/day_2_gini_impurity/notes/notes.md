# PHASE 2 --- MACHINE LEARNING

## WEEK 20 --- DECISION TREES 🌳

### DAY 2 --- HOW DOES A DECISION TREE CHOOSE A SPLIT?

You are now going deeper into the mathematics behind Decision Trees.

### Your Week 20 target:

> **Understand how a Decision Tree evaluates possible splits and chooses
> the best one.**

------------------------------------------------------------------------

# 🎯 DAY 2 OBJECTIVES

By the end of today, you should be able to:

-   Explain **Gini Impurity**
-   Calculate Gini Impurity manually
-   Understand node purity
-   Understand weighted Gini after a split
-   Explain why a tree prefers certain splits
-   Calculate Gini Gain / impurity reduction
-   Understand what `criterion="gini"` actually means in Scikit-learn

------------------------------------------------------------------------

# 1. 🌳 The Core Question

Imagine our dataset contains:

    Age Buys
  ----- ------
     18 No
     20 No
     22 No
     25 Yes
     30 Yes
     35 Yes

A Decision Tree wants to ask:

> **"Which feature and threshold should I use to divide these
> samples?"**

For example:

``` text
Age < 23?
```

creates:

``` text
             Age < 23?
              /      \
            YES       NO
         3 samples  3 samples
```

But how does the tree know whether this is a good split?

That is where impurity comes in.

------------------------------------------------------------------------

# 2. GINI IMPURITY

For a classification node:

$$
Gini = 1 - \sum_{k=1}^{K} p_k^2
$$

where:

-   $p_k$ = proportion of class $k$

For binary classification:

$$
Gini = 1 - (p_{Yes}^2 + p_{No}^2)
$$

------------------------------------------------------------------------

# 3. 🌳 Simple Example

Suppose a node contains:

``` text
8 Yes
2 No
```

Total:

``` text
10
```

Therefore:

$$
p_{Yes} = \frac{8}{10} = 0.8
$$

$$
p_{No} = \frac{2}{10} = 0.2
$$

Now:

$$
Gini = 1 - (0.8^2 + 0.2^2)
$$

$$
= 1 - (0.64 + 0.04)
$$

$$
= 1 - 0.68
$$

$$
\boxed{Gini = 0.32}
$$

### Interpretation

The node is mostly Yes, so it is relatively pure.

------------------------------------------------------------------------

# 4. PURE NODE

Consider:

``` text
10 Yes
0 No
```

Then:

$$
p_{Yes} = 1
$$

$$
p_{No} = 0
$$

Therefore:

$$
Gini = 1 - (1^2 + 0^2)
$$

$$
\boxed{Gini = 0}
$$

A Gini value of 0 means perfectly pure.

``` text
Pure node
    ↓
Gini = 0
```

------------------------------------------------------------------------

# 5. 🏆 MAXIMUM IMPURITY

Now consider:

``` text
5 Yes
5 No
```

Then:

$$
p_{Yes} = 0.5
$$

$$
p_{No} = 0.5
$$

Therefore:

$$
Gini = 1 - (0.5^2 + 0.5^2)
$$

$$
= 1 - (0.25 + 0.25)
$$

$$
\boxed{Gini = 0.5}
$$

For binary classification, 0.5 is the maximum Gini impurity.

So:

``` text
Gini = 0     → completely pure
Gini = 0.5   → maximally mixed
```

------------------------------------------------------------------------

# 6. 🧠 THE IMPORTANT PART: EVALUATING A SPLIT

A tree doesn't simply calculate the Gini of one node.

It asks:

> **"After I make this split, how pure do the resulting child nodes
> become?"**

Suppose:

## Parent

``` text
10 samples

6 Yes
4 No
```

### Parent Gini:

$$
Gini_{parent} = 1 - (0.6^2 + 0.4^2)
$$

$$
= 1 - (0.36 + 0.16)
$$

$$
\boxed{0.48}
$$

Now suppose a split creates:

## Left child

``` text
5 samples

4 Yes
1 No
```

### Gini:

$$
1 - (0.8^2 + 0.2^2)
$$

$$
= 0.32
$$

## Right child

``` text
5 samples

2 Yes
3 No
```

### Gini:

$$
1 - (0.4^2 + 0.6^2)
$$

$$
= 0.48
$$

# 7. ♟️ WEIGHTED GINI

The children have different sizes in general, so we calculate their
weighted impurity.

$$
Gini_{split} =
\frac{N_L}{N}Gini_L +
\frac{N_R}{N}Gini_R
$$

Here:

$$
N_L = 5
$$

$$
N_R = 5
$$

$$
N = 10
$$

Therefore:

$$
Gini_{split} =
\frac{5}{10}(0.32) +
\frac{5}{10}(0.48)
$$

$$
= 0.16 + 0.24
$$

$$
\boxed{0.40}
$$

------------------------------------------------------------------------

# 8. 🚀 GINI GAIN

Now compare:

### Before split

$$
Gini_{parent} = 0.48
$$

### After split

$$
Gini_{split} = 0.40
$$

The reduction is:

$$
GiniGain = Gini_{parent} - Gini_{split}
$$

$$
= 0.48 - 0.40
$$

$$
\boxed{0.08}
$$

So this split reduced impurity by:

$$
\boxed{0.08}
$$

### Key principle:

> A good split significantly reduces impurity.

------------------------------------------------------------------------

# 9. 🧠 How the Decision Tree Actually Thinks

Conceptually, the algorithm does something like:

``` text
Try Feature 1
    ↓
Try threshold A
    ↓
Calculate impurity

Try threshold B
    ↓
Calculate impurity

Try threshold C
    ↓
Calculate impurity

Try Feature 2
    ↓
Try multiple thresholds
    ↓
Calculate impurity

Compare all candidate splits
    ↓
Choose the split producing the
lowest weighted impurity
```

This is one of the most important ideas in Decision Trees.

------------------------------------------------------------------------

# 10. 🔥 Example

Suppose the tree evaluates three possible splits:

  Split       Weighted Gini
  --------- ---------------
  Split A              0.42
  Split B              0.31
  Split C              0.37

The tree prefers:

$$
\boxed{Split\ B}
$$

because:

$$
0.31 < 0.37 < 0.42
$$

In other words:

> Lower resulting impurity = better split.

------------------------------------------------------------------------

# 11. GINI VS GINI GAIN

Do not confuse these.

## Gini Impurity

Measures:

> **How mixed is this node?**

## Gini Gain / Impurity Reduction

Measures:

> **How much did this split improve the situation?**

Conceptually:

$$
\boxed{
Gain = Parent\ Impurity - Weighted\ Child\ Impurity
}
$$


---

# 17. 🎯 DAY 2 SUCCESS CRITERIA

Do not mark Day 2 complete until you can explain these without notes:

- [ ] What is Gini Impurity?
- [ ] Why does a pure node have Gini = 0?
- [ ] Why does a 50/50 binary node have maximum Gini?
- [ ] How do you calculate child-node Gini?
- [ ] Why do we use weighted Gini?
- [ ] What is impurity reduction?
- [ ] How does a Decision Tree compare candidate splits?
- [ ] What does `criterion="gini"` mean?

---

# 🏆 DAY 2 TAKEAWAY

Remember this pipeline:

```text
Candidate Split
      ↓
Create Child Nodes
      ↓
Calculate Gini of Each Child
      ↓
Weight by Child Size
      ↓
Calculate Weighted Gini
      ↓
Compare Candidate Splits
      ↓
Choose Lower Impurity
```

### The mental model:

> Decision Tree = repeatedly find a split that makes the resulting groups more pure.

And mathematically:

$$
\boxed{Best\ Split \rightarrow Lowest\ Weighted\ Child\ Impurity}
$$

---

# 🔥 Your Week 20 trajectory

```text
Day 1 → Decision Tree Fundamentals                 ✅
Day 2 → Gini Impurity & Split Selection           ← YOU ARE HERE
Day 3 → Entropy & Information Gain
Day 4 → Tree Construction + sklearn
Day 5 → Hyperparameters & Overfitting
Day 6 → Visualization + Interpretation
Day 7 → Mini Project: Tree Model
```

### Day 2 mission:

Understand the mathematics, implement Gini from scratch, and manually calculate at least 3 splits.

> Do not rush to `DecisionTreeClassifier`. The goal this week is to understand what the library is doing underneath the API.
