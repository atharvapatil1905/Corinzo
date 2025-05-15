##  Import Libraries

import pandas as pd
import numpy as np
import sys
import os
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    """Load CSV data from a given path."""
    return pd.read_csv(path)

def clean_award_data(df):
    """Remove invalid records (e.g., zero or negative amounts)."""
    df = df[df['Award_Amount'] > 0]
    return df

def add_log_award(df):
    """Add a log-transformed award amount column."""
    df['Log_Award_Amount'] = np.log1p(df['Award_Amount'])
    return df

def encode_categoricals(df):
    """Label encode all relevant categorical columns."""
    encoders = {}
    cols_to_encode = ['Award_Agency', 'Award_Type', 'Performance_Country', 'Performance_State']
    
    for col in cols_to_encode:
        le = LabelEncoder()
        df[col + '_Code'] = le.fit_transform(df[col])
        encoders[col] = le
    
    return df, encoders

def full_pipeline(path):
    """Run full data processing pipeline from raw CSV path."""
    df = load_data(path)
    df = clean_award_data(df)
    df = add_log_award(df)
    df, encoders = encode_categoricals(df)
    return df   

if __name__ == "__main__":
    print("This file is running directly!")

   