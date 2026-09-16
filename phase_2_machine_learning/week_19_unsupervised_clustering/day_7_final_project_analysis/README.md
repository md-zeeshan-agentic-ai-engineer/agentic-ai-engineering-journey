# Week 19 — Unsupervised Learning & Clustering

## Customer Segmentation with K-Means

This project is the final project for **Phase 2 — Week 19** of the AI/ML learning journey.

The purpose of this week is to understand **Unsupervised Learning**, **K-Means Clustering**, **cluster evaluation**, and **customer segmentation**, and then apply these concepts in a complete end-to-end machine learning project.

---

## 📌 Project Overview

Customer segmentation is the process of dividing customers into groups based on similarities in their characteristics or behavior.

In this project, **K-Means Clustering** is used to discover natural groups of customers from the dataset.

Unlike supervised learning, the dataset does not provide predefined target labels such as:

- Premium Customer
- Budget Customer
- Potential Customer

Instead, the algorithm discovers groups from the data, and the resulting clusters are analyzed and interpreted afterward.

The main objective is to answer:

> **What different types of customers exist in the dataset, and what can we learn from these groups?**

---

## 🎯 Objectives

The project focuses on the following objectives:

1. Understand the business problem.
2. Load and inspect the customer dataset.
3. Perform basic data-quality checks.
4. Select meaningful features for clustering.
5. Visualize the customer distribution.
6. Scale the features before distance-based clustering.
7. Determine a reasonable number of clusters.
8. Train a K-Means clustering model.
9. Assign customers to clusters.
10. Visualize the discovered clusters.
11. Analyze cluster centroids.
12. Measure cluster sizes.
13. Profile the characteristics of each cluster.
14. Interpret the discovered customer segments.
15. Translate the ML results into possible business actions.
16. Evaluate the final clustering solution.

---

## 🧠 Machine Learning Concept

### Unsupervised Learning

Unsupervised learning works with data where the desired output or target label is not provided.

Instead of learning:

```text
Input → Known Target
```

the model attempts to discover structure such as:

```text
Input Data → Hidden Patterns / Groups
```

Clustering is one of the major categories of unsupervised learning.

---

## 🔵 K-Means Clustering

K-Means is a clustering algorithm that divides observations into a predefined number of clusters.

The basic process is:

```text
Choose K
   ↓
Initialize centroids
   ↓
Assign each point to the nearest centroid
   ↓
Recalculate centroids
   ↓
Repeat
   ↓
Stop when the clusters stabilize
```

The algorithm attempts to create groups whose observations are relatively close to their corresponding cluster centers.

---

## 📊 Dataset

The project uses the **Mall Customers dataset**.

The dataset contains customer-level information such as:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

The main segmentation features used in the project are based on customer characteristics such as:

- Annual Income
- Spending Score

Additional features may be explored as an extension of the project.

### Dataset File

```text
Mall_Customers.csv
```

---

## 🗂️ Project Structure

```text
week_19_unsupervised_clustering/
│
├── day_1_fundamentals/
│
├── day_2_k-means_algorithm/
│
├── day_3_kmeans_deep_dive/
│
├── day_4_choosing_the_number_of_clusters/
│
├── day_5_scaling_clustering/
│
├── day_6_customer_segmentation/
│
└── day_7_final_project_analysis/
    │
    ├── notebook/
    │   ├── customer_segmentation_final_project.ipynb
    │   └── Mall_Customers.csv
    │
    ├── notes/
    │   └── notes.md
    │
    └── README.md
```

---

## 🛠️ Technologies and Libraries

The project is implemented in Python.

### Core Technologies

- Python
- Jupyter Notebook
- VS Code
- Git

### Python Libraries

```python
numpy
pandas
matplotlib
scikit-learn
```

Optional visualization support:

```python
seaborn
```

---

## 🔧 Main Machine Learning Tools

The project uses the following tools from scikit-learn:

### StandardScaler

Used for feature scaling:

```python
from sklearn.preprocessing import StandardScaler
```

### KMeans

Used to perform clustering:

```python
from sklearn.cluster import KMeans
```

### Silhouette Score

Used to evaluate cluster separation:

```python
from sklearn.metrics import silhouette_score
```

---

## 🔄 Project Workflow

The complete workflow is:

```text
Business Problem
       ↓
Load Dataset
       ↓
Data Inspection
       ↓
Data Quality Checks
       ↓
Feature Selection
       ↓
Exploratory Visualization
       ↓
Feature Scaling
       ↓
Determine K
       ↓
Elbow Method
       ↓
Silhouette Analysis
       ↓
Train K-Means
       ↓
Assign Cluster Labels
       ↓
Visualize Clusters
       ↓
Analyze Centroids
       ↓
Cluster Profiling
       ↓
Business Interpretation
       ↓
Final Evaluation
       ↓
Conclusion
```

---

## 🔍 Feature Scaling

K-Means is based on distance calculations.

Therefore, features with very different numerical scales can affect the clustering process disproportionately.

For this reason, the project uses `StandardScaler`.

Example:

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

The transformation approximately produces features with:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

---

## 📐 Choosing the Number of Clusters

K-Means requires the number of clusters, `K`, to be specified.

The project investigates different values of `K` instead of choosing a value without analysis.

Two important approaches are used:

### 1. Elbow Method

The Elbow Method examines how inertia changes as the number of clusters increases.

```text
K increases
    ↓
Inertia generally decreases
    ↓
Look for a point where the improvement begins to diminish
```

Example implementation:

```python
inertia = []

for k in range(2, 11):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
```

### 2. Silhouette Score

The silhouette score provides information about how well observations fit within their assigned clusters compared with neighboring clusters.

The score generally ranges from:

```text
-1 to +1
```

A higher value generally indicates better-defined separation, but the score should not be interpreted in isolation.

---

## 🤖 Model Training

After selecting a reasonable value of `K`, the final K-Means model is trained.

Example:

```python
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)
```

The resulting cluster labels are added to the original dataset:

```python
df["Cluster"] = clusters
```

> The actual value of `K` should be justified using the results of the analysis rather than assumed beforehand.

---

## 📈 Visualization

The project visualizes the discovered customer groups to make the clustering results easier to understand.

The visualizations include:

- Customer distribution
- Cluster assignments
- Cluster centroids
- Cluster sizes
- Cluster comparisons

Visualization helps connect the mathematical output of K-Means with the underlying customer behavior.

---

## 🎯 Cluster Profiling

After clustering, the project analyzes the characteristics of each cluster.

For example:

```python
cluster_profile = df.groupby("Cluster")[
    ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
].mean()
```

This allows us to compare clusters using their average characteristics.

A cluster might contain customers with:

```text
High income + high spending
```

while another might contain:

```text
High income + low spending
```

The actual interpretation must always be based on the observed dataset.

---

## ⚠️ Important Principle: Cluster IDs Have No Meaning

K-Means may produce labels such as:

```text
Cluster 0
Cluster 1
Cluster 2
Cluster 3
```

These numbers are only identifiers.

For example:

```text
Cluster 0 ≠ automatically Premium Customers
```

Another model run or configuration can assign the same customer group a different cluster number.

Therefore, cluster labels must be interpreted using their actual characteristics.

---

## 💼 Business Interpretation

The ML model produces mathematical groups.

The analyst then studies those groups and translates them into meaningful descriptions.

For example:

| Observed Characteristics | Possible Interpretation |
|---|---|
| High income + high spending | High-value customer segment |
| Low income + low spending | Lower-spending segment |
| High income + low spending | Potential opportunity segment |
| Low income + high spending | High-engagement segment |

These names are examples only.

The final interpretation must be derived from the actual cluster profiles.

---

## 📊 Business Applications

Customer segmentation can support activities such as:

- Personalized marketing
- Customer retention
- Loyalty programs
- Product recommendations
- Promotional campaigns
- Customer relationship management
- Resource allocation
- Audience targeting

The clustering model itself does not determine the correct business decision. It provides a structured way to understand customer groups.

---

## 🧪 Model Evaluation

The project evaluates the clustering solution using:

### Inertia

Measures within-cluster compactness.

Lower inertia generally indicates more compact clusters, but inertia always tends to decrease as more clusters are added, so it should not be used alone to select `K`.

### Silhouette Score

Measures how well observations fit their assigned cluster compared with neighboring clusters.

Example:

```python
score = silhouette_score(
    X_scaled,
    df["Cluster"]
)
```

### Visual Inspection

Cluster plots are also examined for:

- Separation
- Compactness
- Overlap
- Outliers
- Overall structure

### Business Interpretability

A mathematically reasonable clustering solution should also produce groups that can be meaningfully understood for the intended use case.

---

## 📓 Notebook Contents

The final notebook contains the following sections:

```text
1. Business Problem
2. Dataset
3. Data Inspection
4. Data Cleaning
5. Feature Selection
6. Exploratory Data Analysis
7. Feature Scaling
8. Choosing K
9. Elbow Method
10. Silhouette Score
11. K-Means Model Training
12. Cluster Assignment
13. Cluster Visualization
14. Centroid Visualization
15. Cluster Size Analysis
16. Cluster Profiling
17. Cluster Interpretation
18. Business Recommendations
19. Model Evaluation
20. Final Conclusion
```

---

## 🚀 How to Run the Project

### 1. Open the project directory

Open:

```text
day_7_final_project_analysis/notebook/
```

### 2. Open the notebook

Open:

```text
customer_segmentation_final_project.ipynb
```

### 3. Ensure the dataset is available

Make sure:

```text
Mall_Customers.csv
```

is available in the expected notebook location.

### 4. Install required libraries if necessary

```bash
pip install numpy pandas matplotlib scikit-learn seaborn
```

### 5. Run the notebook

Execute the cells from top to bottom.

---

## 🧠 Key Learning Outcomes

After completing this project, I should be able to explain:

- What unsupervised learning is
- What clustering is
- What K-Means does
- What a centroid represents
- Why K is required
- How K-Means assigns observations
- Why feature scaling matters
- What inertia means
- How the Elbow Method works
- What silhouette score measures
- How to profile clusters
- Why cluster IDs have no semantic meaning
- How to interpret discovered groups
- How clustering can support business analysis

---

## 🔥 Extension Challenge

As an additional experiment, compare different feature combinations.

### Experiment 1

Use:

```text
Annual Income
Spending Score
```

### Experiment 2

Use:

```text
Age
Annual Income
Spending Score
```

Then compare:

- Cluster structure
- Optimal K
- Silhouette score
- Cluster profiles
- Interpretability
- Business usefulness

Questions to investigate:

1. Does adding Age change the clusters?
2. Does the selected value of K change?
3. Do the cluster characteristics change?
4. Do the business interpretations change?
5. Which feature combination provides the most useful segmentation for the chosen objective?

---

## 📌 Important Limitations

K-Means has several limitations:

1. The number of clusters must be specified.
2. Results can depend on initialization.
3. It is sensitive to feature scaling.
4. It can be affected by outliers.
5. It generally works best when clusters have reasonably suitable geometric structure.
6. Different feature selections can produce different segmentations.
7. A mathematically defined cluster does not automatically represent a meaningful business segment.
8. Clustering results should be validated against domain knowledge before being used for important decisions.

---

## 🏆 Final Project Goal

The purpose of this project is not simply to execute:

```python
KMeans(...)
```

The real goal is to develop the complete ML reasoning process:

```text
Data
 ↓
Understand
 ↓
Prepare
 ↓
Scale
 ↓
Experiment
 ↓
Evaluate
 ↓
Cluster
 ↓
Profile
 ↓
Interpret
 ↓
Communicate
```

This is the transition from **learning an algorithm** to **using machine learning to solve a practical problem**.

---

## 📚 Week 19 Completion

### Week 19 — Unsupervised Learning & Clustering

```text
Day 1 → Fundamentals
Day 2 → K-Means Algorithm
Day 3 → K-Means Deep Dive
Day 4 → Choosing the Number of Clusters
Day 5 → Scaling & Clustering
Day 6 → Customer Segmentation
Day 7 → Final Project + Analysis
```

### Final Project Output

```text
Customer Segmentation using K-Means
```

### Core Skill Developed

```text
Unsupervised Learning
        +
K-Means Clustering
        +
Cluster Evaluation
        +
Cluster Interpretation
        +
Business Analysis
```

---

## 👨‍💻 Project Status

**Phase:** Phase 2 — Machine Learning

**Week:** Week 19

**Topic:** Unsupervised Learning & Clustering

**Project:** Customer Segmentation with K-Means

**Status:** Completed

---

## 📄 Related Files

```text
notebook/
├── customer_segmentation_final_project.ipynb
└── Mall_Customers.csv

notes/
└── notes.md

README.md
```

---

## ⭐ Final Takeaway

> **K-Means discovers groups; analysis gives those groups meaning.**

A strong clustering project is not judged only by whether the algorithm runs successfully. It should demonstrate a complete chain of reasoning from the original business problem through data preparation, clustering, evaluation, interpretation, and communication of the results.
