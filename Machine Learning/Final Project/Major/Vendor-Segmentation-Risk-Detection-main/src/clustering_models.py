## Import Laibraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import sys
import os

def run_kmeans(X_scaled, n_clusters=4, random_state=42):
    """
    Fit KMeans and return the model and labels.
    """
    model = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = model.fit_predict(X_scaled)
    return model, labels

def elbow_plot(X_scaled, k_range=range(2, 11)):
    """
    Plot the Elbow curve to find optimal number of clusters.
    """
    sse = []
    for k in k_range:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(X_scaled)
        sse.append(model.inertia_)

    plt.figure(figsize=(8, 4))
    plt.plot(list(k_range), sse, marker='o')
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("SSE (Inertia)")
    plt.title("Elbow Method: Optimal k")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def calculate_silhouette(X_scaled, labels):
    """
    Calculate the silhouette score for the given clustering labels.
    """
    score = silhouette_score(X_scaled, labels)
    return round(score, 3)

def reduce_pca(X_scaled, n_components=2):
    """
    Reduce dimensions using PCA and return the components as a DataFrame.
    """
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(X_scaled)
    return pd.DataFrame(components, columns=[f"PCA{i+1}" for i in range(n_components)])


if __name__ == "__main__":
    print("Module test mode: clustering_models")

