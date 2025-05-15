## Import Libraries

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Load final processed data

df = pd.read_csv('./data/processed/vendor_data_with_clusters_anomalies.csv')

st.title("Vendor Segmentation & Risk Detection Dashboard")

## Sidebar filters

st.sidebar.header("Filter Vendors")
cluster_options = sorted(df['Cluster'].unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_options)

anomaly_options = ['All', 'Normal', 'Anomaly']
selected_anomaly = st.sidebar.selectbox("Select Type", anomaly_options)

## Filtered data

filtered_df = df[df['Cluster'] == selected_cluster]
if selected_anomaly != 'All':
    filtered_df = filtered_df[filtered_df['Anomaly'] == selected_anomaly]

st.write(f"Showing {len(filtered_df)} records for Cluster {selected_cluster} ({selected_anomaly})")

## Show table

st.dataframe(filtered_df[['Vendor_Name', 'Award_Amount', 'Award_Type', 'Performance_Country', 'Anomaly']])

## Award amount distribution

st.subheader("Award Amount Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Award_Amount'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

## PCA scatter plot

st.subheader("PCA Cluster View")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='PCA1', y='PCA2', hue='Anomaly', palette={'Normal': 'blue', 'Anomaly': 'red'}, ax=ax2)
ax2.set_title(f"Cluster {selected_cluster} PCA Plot")
st.pyplot(fig2)

