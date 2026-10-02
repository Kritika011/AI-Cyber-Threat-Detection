import pandas as pd
import joblib
import numpy as np

MODEL_PATH = "models/random_forest_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"
FEATURES_PATH = "models/feature_names.pkl"
DATASET_PATH = "dataset/cicids_balanced.csv"


print("Loading model...")

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)
feature_names = joblib.load(FEATURES_PATH)

print("Model loaded successfully!")


# Load one real network-flow record
df = pd.read_csv(DATASET_PATH)

sample = df.iloc[[0]].copy()

# Get the actual label for comparison
actual_label = sample["Label"].iloc[0]

# Remove target
X = sample.drop(columns=["Label"])

# Make sure columns are in the exact order used during training
X = X[feature_names]

# Convert to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Replace infinity
X = X.replace([np.inf, -np.inf], np.nan)

# Fill missing values
X = X.fillna(0)


# Predict
prediction = model.predict(X)

predicted_label = label_encoder.inverse_transform(prediction)[0]


print("\n==============================")
print("PREDICTION RESULT")
print("==============================")

print("Actual label:    ", actual_label)
print("Predicted label: ", predicted_label)


# Prediction probabilities
probabilities = model.predict_proba(X)[0]

confidence = probabilities.max() * 100

print("Confidence:       ", round(confidence, 2), "%")