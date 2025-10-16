import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot_elbow(score, n_components=20):
    X = score[:, :n_components]

    K = range(1, 11)
    inertias = []

    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto")
        kmeans.fit(X)
        # inertia = sum of squared distances to closest cluster center
        inertias.append(kmeans.inertia_) 

    # Plot the elbow curve
    plt.figure(figsize=(8, 5))
    plt.plot(K, inertias, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.xticks(K)
    plt.grid(True)
    plt.show()

