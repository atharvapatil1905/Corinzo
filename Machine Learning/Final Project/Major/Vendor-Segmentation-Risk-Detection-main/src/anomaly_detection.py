## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
import os
import sys

def detect_anomalies(X_scaled, contamination=0.05, random_state=42):
    """
    Fit Isolation Forest and return anomaly labels (-1 for anomaly, 1 for normal).
    """
    model = IsolationForest(contamination=contamination, random_state=random_state)
    labels = model.fit_predict(X_scaled)
    return model, labels

def add_anomaly_column(df, labels):
    """
    Add a new column 'Anomaly' based on Isolation Forest output.
    """
    df['Anomaly'] = pd.Series(labels).map({1: "Normal", -1: "Anomaly"})
    return df

def plot_anomaly_pca(df):
    """
    Scatter plot of PCA components with anomaly color coding.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="PCA1",
        y="PCA2",
        hue="Anomaly",
        palette={"Normal": "blue", "Anomaly": "red"},
        alpha=0.7,
        s=80
    )
    plt.title("Anomaly Detection (Isolation Forest)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Module test mode: anomaly_detection")
    # Optional test code here

