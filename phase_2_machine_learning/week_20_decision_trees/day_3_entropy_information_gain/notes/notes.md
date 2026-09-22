# Phase 2 — Week 20 — Day 3

## Decision Trees: Entropy + Information Gain

**Week 20 Core Focus:** Decision Trees  
**Day 3 Objective:** Understand how a Decision Tree decides whether a split is useful.

Today, we move beyond simply using `DecisionTreeClassifier`. You will understand the mathematics behind the split decision.

---

# 1. The Core Idea

A Decision Tree repeatedly asks:

> “Which feature split makes the resulting groups more pure?”

For classification:

- **Pure group** → mostly/entirely one class
- **Impure group** → mixture of classes

Example:

For classification:

- **Pure group** → mostly/entirely one class
- **Impure group** → mixture of classes

Example:

```text
YES YES YES YES
```

Very pure.

But:

```text
YES NO YES NO
```

Very impure.

The tree tries to create increasingly pure groups.

---

# 2. Entropy

Entropy measures **uncertainty/impurity**.

\[
H(S) = -\sum_i p_i \log_2(p_i)
\]

For binary classification:

\[
H(S) = -p_{Yes}\log_2(p_{Yes}) - p_{No}\log_2(p_{No})
\]

## Important cases

| Distribution | Entropy |
|---|---:|
| 100% Yes, 0% No | 0 |
| 75% Yes, 25% No | 0.811 |
| 50% Yes, 50% No | 1 |
| 25% Yes, 75% No | 0.811 |
| 0% Yes, 100% No | 0 |

So:

- **Higher entropy = more uncertainty**
- **Lower entropy = purer group**

---

# 3. Your Dataset

We have:

| Weather | Play |
|---|---|
| Sunny | No |
| Sunny | No |
| Sunny | Yes |
| Rain | Yes |
| Rain | Yes |
| Rain | No |

There are:

- 3 Yes
- 3 No

Therefore:

\[
P(Yes) = \frac{3}{6} = 0.5
\]

\[
P(No) = \frac{3}{6} = 0.5
\]

## Parent Entropy

\[
H(S) = -(0.5\log_2 0.5 + 0.5\log_2 0.5)
\]

Since:

\[
\log_2(0.5) = -1
\]

we get:

\[
H(S) = 1
\]

**Parent Entropy = 1.0**

This is maximum uncertainty for a binary classification problem.

---

# 4. Split on Weather

Now divide the dataset.

## Sunny group

```text
Sunny → No
Sunny → No
Sunny → Yes
```

So:

- Yes = 1
- No = 2

### Entropy

\[
H(Sunny) =
-\frac{1}{3}\log_2\frac{1}{3}
-\frac{2}{3}\log_2\frac{2}{3}
\]

\[
H(Sunny) \approx 0.918
\]

---

## Rain group

```text
Rain → Yes
Rain → Yes
Rain → No
```

So:

- Yes = 2
- No = 1

Therefore:

\[
H(Rain) \approx 0.918
\]

---

# 5. Weighted Entropy After the Split

This is important.

We don't simply average the two entropies blindly. We weight them according to group size.

\[
H_{split}
=
\frac{3}{6}H(Sunny)
+
\frac{3}{6}H(Rain)
\]

\[
= 0.5(0.918) + 0.5(0.918)
\]

\[
H_{split} \approx 0.918
\]

---

# 6. Information Gain

Information Gain tells us how much uncertainty was removed by the split.

\[
IG = H(Parent) - H(Split)
\]

Therefore:

\[
IG = 1.0 - 0.918
\]

\[
IG \approx 0.082
\]

So the Weather split provides only a small reduction in uncertainty.

---

# 7. The Most Important Insight

Notice what happened:

## Before splitting

The parent group had:

- 3 Yes
- 3 No
- Entropy = 1.0

This means the parent was highly uncertain.

## After splitting on Weather

### Sunny

- 1 Yes
- 2 No
- Entropy ≈ 0.918

### Rain

- 2 Yes
- 1 No
- Entropy ≈ 0.918

### Weighted split entropy

\[
H_{split} \approx 0.918
\]

### Information Gain

\[
IG \approx 0.082
\]

Therefore, the Weather feature reduces uncertainty only slightly.

---

# Core Mental Model

A Decision Tree is essentially asking:

> **“Which split reduces uncertainty the most?”**

The process is:

```text
Parent Dataset
      ↓
Calculate Parent Entropy
      ↓
Try a possible split
      ↓
Calculate entropy of each child group
      ↓
Calculate weighted split entropy
      ↓
Calculate Information Gain
      ↓
Compare with other possible splits
      ↓
Choose the split with the highest Information Gain
```

### Remember

```text
Entropy
   ↓
Measures impurity / uncertainty

Information Gain
   ↓
Measures reduction in impurity / uncertainty

Decision Tree
   ↓
Chooses useful splits that reduce uncertainty
```

---

# 7. The Most Important Insight

Notice what happened:

## Before splitting

```text
YES YES YES
NO  NO  NO
```

Entropy:

```text
1.0
```

## After splitting

```text
Sunny → NO NO YES
Rain  → YES YES NO
```

Both groups are still mixed.

Therefore, the split does not create highly pure groups.

That's why Information Gain is relatively small.

---

# 8. Why This Matters

Imagine another feature produced:

```text
Group A → YES YES YES
Group B → NO NO NO
```

Then:

\[
H(GroupA) = 0
\]

\[
H(GroupB) = 0
\]

Weighted entropy:

\[
0
\]

Therefore:

\[
IG = 1 - 0 = 1
\]

That would be a perfect split.

So the fundamental decision-tree principle is:

> **Choose splits that produce the greatest reduction in uncertainty.**

---

# 9. Entropy vs Information Gain

Don't confuse them.

## Entropy

Measures:

> **How impure is this group?**

## Information Gain

Measures:

> **How much did my split reduce that impurity?**

Think:

```text
Entropy
↓
Measure uncertainty

Split
↓
Create child groups

Information Gain
↓
Measure improvement
```

---

# 10. Your Manual Exercise

Do this **without Scikit-learn first.**

Dataset:

| Weather | Play |
|---|---|
| Sunny | No |
| Sunny | No |
| Sunny | Yes |
| Rain | Yes |
| Rain | Yes |
| Rain | No |

Calculate:

## Task 1

Parent entropy.

## Task 2

Entropy of the Sunny group.

## Task 3

Entropy of the Rain group.

## Task 4

Weighted entropy after splitting on Weather.

## Task 5

Information Gain.

## Task 6

Answer in one sentence:

> Does Weather provide a strong split for this tiny dataset? Why?

---

# 12. Elite-Level Understanding

Don't memorize:

> "`criterion='entropy'` means Information Gain."

Understand the complete chain:

```text
Dataset
    ↓
Measure parent entropy
    ↓
Try possible splits
    ↓
Measure child entropy
    ↓
Calculate weighted impurity
    ↓
Calculate Information Gain
    ↓
Choose the useful split
    ↓
Repeat recursively
```

This is the beginning of understanding why the algorithm makes decisions, rather than merely knowing how to call a library.

---

# 🎯 Day 3 Completion Criteria

Before marking Day 3 complete, you should be able to explain without notes:

- What entropy means
- Why pure groups have entropy 0
- Why a 50/50 binary group has entropy 1
- What Information Gain means
- Why child groups are weighted
- How a Decision Tree uses Information Gain
- Why a split can be valid but still not be useful

## Your key mental model:

> **Entropy measures uncertainty. Information Gain measures how much a split reduces that uncertainty.**

> **A Decision Tree prefers splits that create purer child groups.**

Do the 6 manual calculations first. Then run the code. Don't skip the manual calculation—this is the part that builds the actual understanding.
