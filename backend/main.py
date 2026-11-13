
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import joblib
import io
import os

from datetime import datetime, timezone
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Connect to MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing from .env file")

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=10000)

# Database and collection
db = client["CyberThreatDB"]
history_collection = db["detection_history"]

# Verify database connection
client.admin.command("ping")

app = FastAPI(
    title="AI Cyber Threat Detection API",
    version="1.2"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
        "model": "Random Forest",
        "database": "MongoDB Connected"
    }


def analyze_risk(label, confidence):

    if label == "BENIGN":
        return {
            "risk_score": 0,
            "risk_level": "Low",
            "risk_reason": "Traffic classified as normal."
        }

    critical_attacks = ["Heartbleed", "Infiltration"]

    high_attacks = [
        "DDoS",
        "DoS Hulk",
        "DoS GoldenEye",
        "DoS slowloris",
        "DoS Slowhttptest",
        "Bot"
    ]

    if label in critical_attacks:
        score = 95
        level = "Critical"
        reason = f"{label} is classified as a potentially critical threat."

    elif label in high_attacks:
        score = 85
        level = "High"
        reason = f"{label} is classified as a high-risk attack."

    elif confidence >= 70:
        score = 70
        level = "High"
        reason = f"{label} detected with relatively high model confidence."

    else:
        score = 45
        level = "Medium"
        reason = f"{label} detected, but model confidence is lower."

    return {
        "risk_score": score,
        "risk_level": level,
        "risk_reason": reason
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file."
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not read CSV file."
        )

    if df.empty:
        raise HTTPException(
            status_code=400,
            detail="CSV contains no data rows."
        )

    missing_features = [
        feature for feature in feature_names
        if feature not in df.columns
    ]

    if missing_features:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Missing required features.",
                "missing_features": missing_features
            }
        )

    X = df[feature_names].copy()
    X = X.apply(pd.to_numeric, errors="coerce")
    X = X.replace([np.inf, -np.inf], np.nan)
    X = X.fillna(0)

    # ML prediction
    predictions = model.predict(X)
    labels = label_encoder.inverse_transform(predictions)
    probabilities = model.predict_proba(X)

    results = []

    for i, label in enumerate(labels):

        confidence = float(probabilities[i].max() * 100)

        risk = analyze_risk(str(label), confidence)

        results.append({
            "flow_id": i + 1,
            "prediction": str(label),
            "confidence": round(confidence, 2),
            "risk_score": risk["risk_score"],
            "risk_level": risk["risk_level"],
            "risk_reason": risk["risk_reason"]
        })

    # Save predictions in MongoDB
    try:
        current_time = datetime.now(timezone.utc)

        documents = []

        for result in results:
            document = {
                **result,
                "filename": file.filename,
                "detected_at": current_time
            }
            documents.append(document)

        history_collection.insert_many(documents)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Prediction completed, but saving to MongoDB failed."
        )

    return {
        "filename": file.filename,
        "total_flows": len(results),
        "saved_to_database": True,
        "saved_count": len(results),
        "results": results
    }


# View previous detection history
@app.get("/history")
def get_history(limit: int = Query(default=20, ge=1, le=100)):

    records = list(
        history_collection.find()
        .sort("_id", -1)
        .limit(limit)
    )

    for record in records:
        record["_id"] = str(record["_id"])
        record["detected_at"] = record["detected_at"].isoformat()

    return {
        "total_records": len(records),
        "history": records
    }
