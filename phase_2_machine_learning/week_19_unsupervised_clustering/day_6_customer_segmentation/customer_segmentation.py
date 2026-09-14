### 24. Complete Day 6 Code

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# 1. Load data
df = pd.read_csv("Mall_Customers.csv")


# 2. Explore data
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())


# 3. Select features
X = df[["Annual Income", "Spending Score"]]


# 4. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 5. Find suitable K
inertia = []
silhouette_scores = []

for k in range(2, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    inertia.append(model.inertia_)
    silhouette_scores.append(
        silhouette_score(X_scaled, labels)
    )


# 6. Plot Elbow Method
plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    inertia,
    marker="o"
)

plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()


# 7. Plot Silhouette Score
plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    silhouette_scores,
    marker="o"
)

plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")

plt.show()


# 8. Train final K-Means model
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)


# 9. Analyze clusters
cluster_summary = df.groupby("Cluster")[
    ["Age", "Annual Income", "Spending Score"]
].mean()

print(cluster_summary)


# 10. Cluster sizes
print(
    df["Cluster"]
    .value_counts()
    .sort_index()
)


# 11. Visualize clusters
plt.figure(figsize=(10, 6))

plt.scatter(
    df["Annual Income"],
    df["Spending Score"],
    c=df["Cluster"]
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.show()