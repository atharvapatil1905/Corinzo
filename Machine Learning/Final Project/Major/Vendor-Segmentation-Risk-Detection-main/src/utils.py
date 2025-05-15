## Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_award_distribution(df):
    """
    Plot histogram of award amounts.
    """
    plt.figure(figsize=(8, 4))
    sns.histplot(df['Award_Amount'], bins=50, kde=True)
    plt.title("Award Amount Distribution")
    plt.xlabel("Award Amount ($)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def save_df(df, path):
    """
    Save DataFrame to a CSV file.
    """
    df.to_csv(path, index=False)
    print(f"Data saved to {path}")

def summarize_clusters(df):
    """
    Print average stats per cluster.
    """
    summary = df.groupby("Cluster")[["Award_Amount", "Log_Award_Amount"]].mean().round(2)
    print("Cluster Summary:\n", summary)
    return summary

if __name__ == "__main__":
    print("Module test mode: utils")