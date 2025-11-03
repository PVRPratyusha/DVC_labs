"""Modify housing data to simulate data changes"""
import pandas as pd

# Load original data
df = pd.read_csv('data/housing_data.csv')

print(f"Original data shape: {df.shape}")

# Simulate data change: Keep only houses with MedInc > 5
df_modified = df[df['MedInc'] > 5].reset_index(drop=True)

print(f"Modified data shape: {df_modified.shape}")
print(f"Removed {len(df) - len(df_modified)} rows")

# Save modified data
df_modified.to_csv('data/housing_data.csv', index=False)
print("Data saved!")
