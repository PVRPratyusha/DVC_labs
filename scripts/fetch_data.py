"""Fetch California Housing dataset and save to CSV"""
from sklearn.datasets import fetch_california_housing
import pandas as pd
import os

# Fetch dataset
print("Fetching California Housing dataset...")
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Save to data folder
output_path = 'data/housing_data.csv'
df.to_csv(output_path, index=False)
print(f"Dataset saved to {output_path}")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
