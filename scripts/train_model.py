"""Train a model to predict California house prices"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import json
import os

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Load data
print("Loading data...")
df = pd.read_csv('data/housing_data.csv')

# Prepare features and target
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# Train model
print("\nTraining Random Forest model...")
model = RandomForestRegressor(n_estimators=50, random_state=42, max_depth=10)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Performance:")
print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Save metrics
metrics = {
    'mse': float(mse),
    'r2_score': float(r2),
    'train_samples': len(X_train),
    'test_samples': len(X_test)
}

with open('results/metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

# Save predictions
results_df = pd.DataFrame({
    'actual': y_test.values,
    'predicted': y_pred
})
results_df.to_csv('results/predictions.csv', index=False)

print("\nResults saved to results/ folder")
