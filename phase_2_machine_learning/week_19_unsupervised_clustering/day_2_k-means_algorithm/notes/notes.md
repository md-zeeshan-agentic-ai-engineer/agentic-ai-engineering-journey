# Phase 2 — Week 19 — Day 2
# Unsupervised Learning: K-Means Clustering

## Week 19 Goal

By the end of this week, you should be able to:

- Understand unsupervised learning
- Explain clustering
- Understand the K-Means algorithm
- Choose an appropriate value of K
- Understand centroids and Euclidean distance
- Evaluate clustering using inertia and silhouette score
- Implement K-Means using `scikit-learn`
- Apply clustering to a realistic dataset
- Interpret and visualize clusters

---

# Day 2 — K-Means Algorithm

## 1. What is K-Means?

K-Means is an **unsupervised machine learning algorithm** used to divide data into **K clusters**.

The algorithm tries to put **similar data points into the same cluster**.

### Example

Imagine a company has customer data:

| Customer | Annual Income | Spending Score |
|---|---:|---:|
| A | 25,000 | 20 |
| B | 27,000 | 25 |
| C | 80,000 | 85 |
| D | 82,000 | 90 |
| E | 50,000 | 45 |

In supervised learning, we might already have labels such as:

```text
Customer A → Group 1
Customer B → Group 1
Customer C → Group 2
...
```

With K-Means, we **do not provide these labels**.

Instead:

> K-Means discovers groups automatically.

---

## 2. How K-Means Works

The basic process is:

```text
Choose K
    ↓
Initialize K centroids
    ↓
Assign each point to its nearest centroid
    ↓
Recalculate the centroids
    ↓
Repeat
    ↓
Stop when the clusters stabilize
```

This is the **core K-Means algorithm** you should remember.

### Step-by-step

1. **Choose K**
   - Decide how many clusters you want.

2. **Initialize K centroids**
   - Select initial center points for the clusters.

3. **Assign each point to its nearest centroid**
   - Calculate the distance between each data point and the centroids.
   - Assign the point to the closest centroid.

4. **Recalculate the centroids**
   - For each cluster, calculate the mean of its data points.
   - This mean becomes the new centroid.

5. **Repeat**
   - Reassign points to the nearest centroids.
   - Recalculate the centroids again.

6. **Stop when the clusters stabilize**
   - The algorithm stops when the assignments/centroids no longer change significantly, or another stopping criterion is reached.

---

## Key Idea to Remember

K-Means repeatedly performs two main operations:

```text
Assign points → Update centroids → Repeat
```

Or, more simply:

> **Find the nearest centroid, then move each centroid to the mean of its cluster.**

---

## Important Terms

### K

`K` represents the **number of clusters** we want to create.

Example:

```python
K = 3
```

means we want the algorithm to create **3 clusters**.

### Centroid

A **centroid** is the center of a cluster.

For a cluster, the centroid is calculated as the mean of the feature values of the points belonging to that cluster.

### Cluster

A **cluster** is a group of data points that are relatively similar to one another.

### Unsupervised Learning

In unsupervised learning, the training data does **not** contain predefined target labels.

K-Means discovers patterns or groups in the data automatically.

---

## Core Mental Model

Think of K-Means like this:

```text
Data Points
     ↓
Choose K
     ↓
Place K centers
     ↓
Find nearest center for every point
     ↓
Move centers to the average of their points
     ↓
Repeat until stable
```

The most important sequence to remember is:

**Choose K → Initialize centroids → Assign → Recalculate → Repeat → Stabilize**


---

## 3. Step 1 — Choose K

`K` represents the **number of clusters** we want.

For example:

```python
K = 3
```

means:

> Divide the dataset into 3 clusters.

### How do we choose K?

The difficult part is that K-Means usually does **not know the correct value of K automatically**.

We therefore need techniques such as:

- **Elbow Method**
- **Silhouette Score**
- **Domain Knowledge**

We will study these techniques more deeply later.

---

## 4. Step 2 — Initialize Centroids

A **centroid** is the **center point of a cluster**.

Suppose we choose:

```text
K = 3
```

K-Means initially creates three centroids:

```text
Centroid 1
Centroid 2
Centroid 3
```

Modern implementations such as `scikit-learn` commonly use an initialization strategy called **K-Means++**, which generally gives better starting positions than purely random initialization.

---

## 5. Step 3 — Assign Points to the Nearest Centroid

K-Means calculates the **distance between every data point and each centroid**.

The most common distance is **Euclidean distance**.

### Euclidean Distance

For two points:

```text
A = (x₁, y₁)
B = (x₂, y₂)
```

the Euclidean distance is:

\[
d(A,B) = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
\]

The point is assigned to **whichever centroid is closest**.

### Example

Suppose we have **Point P**:

```text
Distance to C1 = 2.1
Distance to C2 = 5.7
Distance to C3 = 3.4
```

The smallest distance is:

```text
2.1
```

Therefore:

```text
P → Cluster 1
```

### Key Idea

> **Each data point is assigned to the nearest centroid based on distance.**

---

## 6. Step 4 — Recalculate Centroids

After assigning all points to clusters, K-Means calculates a **new centroid for each cluster**.

### For one-dimensional data

Suppose the data points are:

```text
10, 12, 14
```

The centroid is the mean:

\[
\frac{10 + 12 + 14}{3} = 12
\]

Therefore:

```text
Centroid = 12
```

### For two-dimensional points

Suppose we have:

```text
(2, 4)
(4, 6)
(6, 8)
```

The centroid is calculated separately for the `x` and `y` coordinates.

For the `x` coordinate:

\[
x = \frac{2 + 4 + 6}{3} = 4
\]

For the `y` coordinate:

\[
y = \frac{4 + 6 + 8}{3} = 6
\]

So:

```text
Centroid = (4, 6)
```

> **A centroid is the mean position of all points belonging to a cluster.**

---

## 7. Step 5 — Repeat

K-Means repeatedly performs:

```text
Assign points
      ↓
Update centroids
      ↓
Assign points again
      ↓
Update centroids again
      ↓
      ...
```

Eventually, the assignments stop changing significantly.

Then the algorithm stops.

> K-Means alternates between **assigning points** and **updating centroids** until convergence.

---

# 8. Important Concepts

## K

**K** is the number of clusters.

Example:

```python
n_clusters = 3
```

means:

```text
K = 3
```

The algorithm will create **3 clusters**.

---

## Centroid

The **center of a cluster**.

A centroid is calculated from the **mean of the points belonging to that cluster**.

Example:

```text
Points:
(2, 4)
(4, 6)
(6, 8)

Centroid:
(4, 6)
```

---

## Cluster Assignment

The **cluster to which a data point belongs**.

Example:

```text
Customer A → Cluster 0
Customer B → Cluster 0
Customer C → Cluster 2
```

In `scikit-learn`, cluster labels commonly start from `0`.

---

## Iteration

One cycle of:

```text
Assignment → Centroid Update
```

K-Means performs multiple iterations until **convergence**.

---

## Euclidean Distance

Euclidean distance measures the **straight-line distance between two points**.

It is especially important for K-Means because **cluster assignment is based on distance**.

For two points:

```text
A = (x₁, y₁)
B = (x₂, y₂)
```

the Euclidean distance is:

\[
d(A,B) = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
\]

---

# 9. Inertia

One of the most important K-Means concepts is **inertia**.

Inertia measures the **total squared distance between each point and the centroid of its assigned cluster**.

Conceptually:

\[
\text{Inertia}
=
\sum_{i=1}^{n}
\text{distance}(x_i,\text{centroid}_{cluster_i})^2
\]

### Interpretation

Lower inertia generally means that points are **closer to their assigned centroids**.

However:

> **Lower inertia alone does not mean that the clustering is better.**

### Why?

Because increasing `K` almost always decreases inertia.

For example:

```text
K = 2 → inertia = 5000
K = 3 → inertia = 3000
K = 4 → inertia = 1900
K = 5 → inertia = 1300
```

As `K` increases, inertia generally decreases.

Therefore, we need a method for selecting a **useful K** rather than simply choosing the K with the lowest inertia.

This leads us to the **Elbow Method**, which we will study next.

---

## Quick Summary

```text
K
→ Number of clusters

Centroid
→ Center of a cluster

Cluster Assignment
→ Which cluster a point belongs to

Iteration
→ Assignment + Centroid Update

Euclidean Distance
→ Straight-line distance between points

Inertia
→ Total squared distance from points to their assigned centroids
```

### K-Means Core Loop

```text
Choose K
   ↓
Initialize centroids
   ↓
Assign points to nearest centroid
   ↓
Recalculate centroids
   ↓
Repeat
   ↓
Converge
```

# 19. Important Limitation: Feature Scaling

K-Means is distance-based.

Therefore, feature scale can strongly affect the result.

Imagine:

Age:       18–70
Salary:    20,000–2,000,000

Salary has a much larger numerical scale.

Without scaling, salary could dominate the distance calculation.

Therefore, K-Means often works better after feature scaling.

Example:


# 20. K-Means Strengths
- Advantages
- Simple to understand
- Fast for many datasets
- Easy to implement
- Works well for compact, well-separated clusters
- Easy to visualize
- Useful for customer segmentation and exploratory analysis

# 21. K-Means Limitations

K-Means is not perfect.

### 1. You need to choose K
How many clusters should I create?

The algorithm does not inherently know.

### 2. Sensitive to feature scale

Large-scale features can dominate distance calculations.

### 3. Sensitive to outliers

Extreme points can pull centroids away from the main group.

### 4. Assumes roughly compact clusters

K-Means can struggle with unusual shapes such as:

Moon-shaped clusters
Ring-shaped clusters
Highly irregular clusters
### 5. Different initializations can produce different results

This is one reason random_state and K-Means++ initialization are useful.

# 22. Real-World Applications

### K-Means is commonly used for:

Customer Segmentation
Cluster 1 → Low income / low spending
Cluster 2 → High income / high spending
Cluster 3 → High income / low spending
Image Compression

Similar colors can be grouped into clusters.

Document Clustering

Similar documents can be grouped together.

Product Segmentation

Products with similar characteristics can be grouped.

Anomaly Exploration

Very distant points may deserve further investigation, although K-Means itself is not primarily an anomaly-detection algorithm.

# 23. Today's Mental Model

You should be able to explain K-Means without code:

K-Means chooses K cluster centers, assigns every point to the nearest center, recalculates the centers using the assigned points, and repeats this process until the clusters stabilize.

If you can explain that clearly, you understand the core algorithm.

# Day 2 Checklist

Before moving to Day 3, make sure you can answer yes to these:

 - What is K-Means?
 - What does K represent?
 - What is a centroid?
 - Why does K-Means use distance?
 - What is Euclidean distance?
 - How are cluster assignments made?
 - How are centroids updated?
 - What is inertia?
 - Why is feature scaling important?
 - What is the difference between fit() and predict()?
 - Can I implement K-Means using scikit-learn?
 - Can I visualize the resulting clusters?
 - Can I explain the algorithm without looking at my notes?

# Day 2 Outcome

Skill Output: K-Means clustering + centroid-based grouping

Project Output: notebooks/kmeans_basics.ipynb

Next logical step: Day 3 — Choosing K with the Elbow Method + Silhouette Score.

This completes the core algorithm understanding from your Week 19 — Unsupervised Learning roadmap and moves you toward actually deciding whether your clustering is good.