# Vendor Segmentation & Procurement Risk Detection

A machine learning project that segments vendors using unsupervised learning and detects procurement anomalies using Isolation Forest. It analyzes vendor transaction patterns from 2021 to 2024 and visualizes the insights through an interactive dashboard.

---

## 📚 Table of Contents

- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [How to Run](#how-to-run)
- [Results](#results)
- [Author](#author)
- [Future Improvements](#future-improvements)

---

## 📌 About the Project

This project clusters vendors using **K-Means** based on spending patterns and delivery behavior, and flags risky transactions using **Isolation Forest**. It uses synthetic-but-realistic data simulating U.S. federal award activity between 2021 and 2024.

The pipeline includes:

- Data preprocessing & feature engineering
- Vendor segmentation
- Procurement risk detection
- Streamlit-based dashboard

---

## 🛠 Technologies Used

- Python 3.13
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

---

## ✨ Features

- 🧹 Feature Engineering:

  - Log-transformed award amounts
  - Label-encoded categorical features
  - PCA-based dimensionality reduction

- 📊 Clustering & Risk Detection:

  - K-Means clustering (elbow + silhouette)
  - Isolation Forest anomaly detection

- 📈 Dashboard:
  - Visualizes cluster distributions
  - Filters by cluster and anomaly
  - Interactive histograms and scatter plots

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/vendor-segmentation-risk-detection.git
   cd vendor-segmentation-risk-detection
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # On Windows
   pip install -r requirements.txt
   ```

3. **Run Notebooks**

   - `01_data_preparation.ipynb`
   - `02_segmentation_clustering.ipynb`
   - `03_risk_detection.ipynb`

4. **Launch the Streamlit Dashboard**
   ```bash
   streamlit run notebook/04_dashboard.py
   ```

---

## 📊 Results

- Vendors grouped into 3–5 distinct clusters
- Outliers flagged as "Anomaly" using Isolation Forest
- Dashboard enables filtering, analysis, and visual insights

Sample Outputs:

- Cluster Silhouette Score: ~0.63
- Anomalies Detected: 4.9% of total records

---

## 👩‍💻 Author

**Aakanksha Haravde**  
Computer Engineer | MBA AI-ML  
GitHub: [github.com/aakanksha](https://github.com/your-github-profile)

---

## 🚀 Future Improvements

- Apply advanced clustering: DBSCAN, GMM
- Incorporate time-series based anomaly detection
- Extend dashboard with cost-saving simulations
- Use real-world datasets (e.g., USAspending.gov live data)

---

## ✅ Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

MIT License – open for academic and personal use.
