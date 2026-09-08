# DAY 1 — Unsupervised Learning Fundamentals

Welcome to Day 1 of Unsupervised Learning.

Today we will build the foundation for understanding **Unsupervised Machine Learning**. The goal is not just to memorize definitions, but to understand why unsupervised learning exists, how it differs from supervised learning, and where it is used in real ML projects.

## 1. What Is Machine Learning?

Machine Learning is a way of teaching a computer to learn patterns from data and use those patterns to make decisions or predictions.

There are three major learning paradigms:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

Today we focus on **Unsupervised Learning**.


# 2. Supervised vs Unsupervised Learning

The most important difference is:

> Does the training data contain a known target/label?

## Supervised Learning

In supervised learning, we have:

**Features → Model → Known Target**

For example:

```text
House Size + Location → Model → House Price
```

Suppose we have:

| House Size | Location | Price |
|---|---|---|
| 1000 sq ft | Delhi | ₹50L |
| 1500 sq ft | Delhi | ₹75L |
| 2000 sq ft | Mumbai | ₹1.2Cr |

Here:

- House Size = Feature
- Location = Feature
- House Price = Target/Label

The model learns:

```text
Features → Target
```

After training, we can give it a new house:

```text
1800 sq ft + Mumbai
        ↓
      Model
        ↓
Predicted Price
```

## Common supervised learning tasks

### Regression

Predict a numerical value.

```text
House features → House price
```

### Classification

Predict a category.

```text
Email features → Spam / Not Spam
```

# 3. Unsupervised Learning

In unsupervised learning, there is **no known target variable**.

The basic structure is:

```text
Features → Model → Hidden Patterns / Groups
```

For example:

```text
Customer Spending
Customer Visits
Customer Age
       ↓
     Model
       ↓
Discover Groups
```

The algorithm may discover groups such as:

```text
Group 1 → Budget Customers
Group 2 → Regular Customers
Group 3 → Premium Customers
```

The important point is:

> We did not tell the algorithm which customer belongs to which group.

The algorithm attempts to discover structure in the data itself.


# 4. A Simple Real-World Example

Imagine an online store has 10,000 customers.

For every customer, we know:

```text
Age
Number of Visits
Total Spending
Average Order Value
```

But we don’t have a label saying:

```text
Customer Type = Budget
Customer Type = Regular
Customer Type = Premium
```

We can use unsupervised learning.

```text
Age
Visits
Spending
Order Value
      ↓
Unsupervised Learning Algorithm
      ↓
Discover Natural Groups
```

The algorithm might discover:

# Group A

```text
Low spending
Few visits
```

→ Budget customers

# Group B

```text
Medium spending
Regular visits
```

→ Regular customers

# Group C

```text
High spending
Frequent visits
```

→ Premium customers

Notice something important:

> The algorithm discovered the groups.

> We did not provide the labels beforehand.

# 5. What Does "Unsupervised" Actually Mean?

Think of it this way.

## Supervised

You give the student:

> "Here are 100 questions and their correct answers. Learn the relationship."

The student learns:

```text
Question → Correct Answer
```

## Unsupervised

You give the student:

> "Here are 100 objects. Organize them into meaningful groups."

The student has to discover:

```text
Objects → Patterns → Groups
```

That is the basic intuition behind unsupervised learning.

# 6. Why Do We Need Unsupervised Learning?

Because in real-world datasets, **labels are often unavailable, expensive, or difficult to create.**

Imagine a company has:

```text
10 million customers
```

It may have information such as:

```text
Age
Location
Purchases
Visits
Browsing behavior
Time spent
```

But manually assigning:

```text
Customer Type
```

to every customer could be extremely expensive.

Unsupervised learning can help discover useful structures automatically.

# 7. The Four Key Concepts for Today

Your Day 1 roadmap contains four major areas.

## ① Clustering

Finding similar observations and grouping them together.

Example:

```text
Customers
   ↓
Clustering
   ↓
Group 1
Group 2
Group 3
```

Popular algorithms:

- K-Means
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models

We will study these in detail later.

# 8. Dimensionality Reduction

Sometimes a dataset contains hundreds or thousands of features.

For example:

```text
Dataset
   ↓
500 features
```

Working with 500 dimensions can be difficult.

Dimensionality reduction attempts to represent the important information using fewer dimensions.

For example:

```text
500 features
      ↓
Dimensionality Reduction
      ↓
2 or 3 important dimensions
```

Popular techniques include:

- PCA
- t-SNE
- UMAP

One major application is visualization.

## Visualization Example

Imagine a dataset with:

```text
100 features
```

We cannot directly visualize 100 dimensions.

We can potentially reduce it to:

```text
100 dimensions
      ↓
     PCA
      ↓
2 dimensions
      ↓
    Plot
```

Then we can visually inspect patterns.

# 9. Association Learning

Association learning tries to discover relationships between items or events.

A classic example is **Market Basket Analysis**.

Suppose customers frequently purchase:

```text
Bread
Milk
Butter
```

The algorithm may discover relationships such as:

```text
Bread → Milk
```

or:

```text
Milk + Bread → Butter
```

This can be useful for:

- Recommendation systems
- Cross-selling
- Product placement
- E-commerce
- Retail analytics

A famous example is:

```text
Customers who buy X often also buy Y.
```
# 10. When Labels Are Unavailable

This is one of the most important reasons to use unsupervised learning.

Suppose you have:

```text
Customer ID
Age
Income
Visits
Spending
```

but no:

```text
Customer Segment
```

Then supervised learning cannot directly learn the customer segment because the target is missing.

Unsupervised learning can instead search for patterns:

```text
Customer Data
      ↓
Unsupervised Learning
      ↓
Natural Structure
      ↓
Customer Segments
```
# 11. Supervised vs Unsupervised — Important Comparison

| Property | Supervised | Unsupervised |
|---|---|---|
| Target available? | ✅ Yes | ❌ No |
| Main goal | Predict target | Discover structure |
| Labels required? | Yes | No |
| Example | House price prediction | Customer segmentation |
| Common task | Classification | Clustering |
| Common task | Regression | Dimensionality reduction |
| Output | Prediction | Groups/patterns/representations |

## Remember this:

```text
SUPERVISED
Features → Target
```

```text
UNSUPERVISED
Features → Hidden Structure
```

This single distinction will help you understand most introductory ML discussions.


# 12. Important Terminology

You should become comfortable with these terms.

## Feature

An input variable.

Example:

```text
Age
Income
Spending
```

## Target / Label

The known answer we want to predict.

Example:

```text
House Price
```

## Observation / Sample

One individual data point.

Example:

```text
Customer #101
```

## Cluster

A group of observations that are considered similar according to some criteria.

Example:

```text
Cluster 1 → Budget Customers
Cluster 2 → Regular Customers
Cluster 3 → Premium Customers
```

## Pattern

A meaningful structure or relationship found in data.

# 13. Very Important: The Algorithm Does Not Automatically Know the Meaning of a Cluster

Suppose K-Means produces:

```text
Cluster 0
Cluster 1
Cluster 2
```

The algorithm does **not** inherently know:

```text
Cluster 0 = Budget
Cluster 1 = Premium
Cluster 2 = Regular
```

Those names are assigned by us after analyzing the characteristics of each cluster.

For example:

```text
Cluster 0
Average spending = ₹2,000
Few visits
```

We might interpret it as:

```text
Budget Customers
```

Whereas:

```text
Cluster 2
Average spending = ₹50,000
Frequent visits
```

might be interpreted as:

```text
Premium Customers
```

This distinction is extremely important.


# 14. Unsupervised Learning Is Not "Finding the Truth"

Another important concept:

> **Unsupervised algorithms discover mathematical structure, not necessarily human-meaningful categories.**

For example, an algorithm may create:

```text
Cluster A
Cluster B
Cluster C
```

But whether those clusters represent useful business categories depends on:

- Feature selection
- Data quality
- Scaling
- Distance metric
- Algorithm choice
- Number of clusters
- Domain knowledge

Therefore, interpretation matters.

# 15. Practical Task — Day 1

Let's perform the exercise from your roadmap.

Consider this small dataset:

| Customer | Age | Visits/Month | Spending/Month |
|---|---:|---:|---:|
| A | 22 | 2 | ₹1,500 |
| B | 25 | 3 | ₹2,000 |
| C | 24 | 2 | ₹1,800 |
| D | 35 | 8 | ₹8,000 |
| E | 38 | 9 | ₹9,000 |
| F | 34 | 7 | ₹7,500 |
| G | 48 | 15 | ₹30,000 |
| H | 52 | 17 | ₹35,000 |
| I | 50 | 16 | ₹32,000 |

Try to identify natural groups without being given labels.
# You may observe:

## Group 1

```text
A, B, C
```

### Characteristics:

```text
Low visits
Low spending
Younger customers
```

### Possible interpretation:

```text
Budget / Low-Engagement Customers
```

## Group 2

```text
D, E, F
```

### Characteristics:

```text
Moderate visits
Moderate spending
```

### Possible interpretation:

```text
Regular Customers
```

## Group 3

```text
G, H, I
```

### Characteristics:

```text
High visits
High spending
```

### Possible interpretation:

```text
Premium / High-Value Customers
```
# 16. What We Just Did

Notice that we started with:

```text
Customer Data
```

There was no:

```text
Customer Type
```

Then we examined:

```text
Age
Visits
Spending
```

and manually discovered:

```text
Natural Groups
```

This is the fundamental intuition behind clustering.

Later, an algorithm such as K-Means will perform this grouping mathematically.

# 17. Mental Model for Day 1

Remember this pipeline:

                 MACHINE LEARNING
                       │
          ┌────────────┴────────────┐
          │                         │
     SUPERVISED                UNSUPERVISED
          │                         │
     Known Target              No Target
          │                         │
     Prediction              Discover Structure
          │                         │
   ┌──────┴──────┐          ┌──────┴──────────┐
   │             │          │        │        │
Regression  Classification  Clustering  PCA  Association

# Day 1 Learning Objectives

By the end of today, you should be able to explain:

- What supervised learning is
- What unsupervised learning is
- The difference between features and targets
- Why labels may be unavailable
- What clustering means
- What dimensionality reduction means
- What association learning means
- Why customer segmentation is an unsupervised learning problem
- Why clusters do not automatically have meaningful names
- How to manually identify natural groups in a dataset

# Day 1 Interview Questions

## Q1. What is the main difference between supervised and unsupervised learning?

**Answer:**

Supervised learning learns from labeled data with a known target, while unsupervised learning works without target labels and attempts to discover hidden patterns or structures in the data.

---

## Q2. Is clustering supervised or unsupervised?

**Answer:**

Clustering is an unsupervised learning technique because the algorithm groups observations without being given predefined class labels.

---

## Q3. Give a real-world example of unsupervised learning.

**Answer:**

Customer segmentation based on customer behavior such as spending, visit frequency, and purchase patterns.

---

## Q4. Why is customer segmentation often unsupervised?

**Answer:**

Because companies may have customer behavior data but no predefined customer categories. An unsupervised algorithm can discover natural groups within the data.

---

## Q5. What is dimensionality reduction?

**Answer:**

Dimensionality reduction is the process of representing high-dimensional data using fewer dimensions while attempting to preserve important information.

# Day 1 Notes

Write this at the top of your notes:

DAY 1 — UNSUPERVISED LEARNING

Supervised:
Features → Model → Known Target

Unsupervised:
Features → Model → Hidden Patterns / Groups

Main Unsupervised Tasks:
1. Clustering
2. Dimensionality Reduction
3. Association Learning

Key Use Case:
Customer Segmentation

Core Idea:
No predefined labels → discover structure from data

# One sentence to remember

Supervised Learning asks: "What should I predict?" — Unsupervised Learning asks: "What structure exists in my data?"

Day 1 foundation complete.