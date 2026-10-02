from fastapi import FastAPI, UploadFile, File
import pandas as pd
import numpy as np
import joblib
import io

app = FastAPI(
    title="AI Cyber Threat Detection API",
    version="1.0"
)

# Load trained ML files
model = joblib.load("models/random_forest_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
feature_names = joblib.load("models/feature_names.pkl")


@app.get("/")
def root():
    return {
        "message": "AI Cyber Threat Detection API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "Random Forest"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read uploaded CSV
    contents = await file.read()

    df = pd.read_csv(io.BytesIO(contents))

    # Keep only features used during training
    missing_features = [
        feature for feature in feature_names
        if feature not in df.columns
    ]

    if missing_features:
        return {
            "error": "Uploaded CSV is missing required features",
            "missing_features": missing_features
        }

    X = df[feature_names].copy()

    # Convert to numeric
    X = X.apply(pd.to_numeric, errors="coerce")

    # Replace infinity
    X = X.replace([np.inf, -np.inf], np.nan)

    # Fill missing values
    X = X.fillna(0)

    # Predict
    predictions = model.predict(X)

    labels = label_encoder.inverse_transform(predictions)

    # Prediction probabilities
    probabilities = model.predict_proba(X)

    results = []

    for i, label in enumerate(labels):

        confidence = float(probabilities[i].max() * 100)

        # Simple project risk classification
        if label == "BENIGN":
            risk = "Low"
        elif confidence >= 90:
            risk = "High"
        elif confidence >= 70:
            risk = "Medium"
        else:
            risk = "Low"

        results.append({
            "prediction": label,
            "confidence": round(confidence, 2),
            "risk": risk
        })

    return {
        "filename": file.filename,
        "total_flows": len(results),
        "results": results
    }