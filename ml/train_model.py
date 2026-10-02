import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# 1. SETTINGS
# ==========================================

DATASET_PATH = "dataset/cicids_balanced.csv"
MODEL_PATH = "models/random_forest_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"
FEATURES_PATH = "models/feature_names.pkl"

RANDOM_STATE = 42


# ==========================================
# 2. LOAD DATASET
# ==========================================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print("Dataset shape:", df.shape)


# ==========================================
# 3. CLEAN COLUMN NAMES
# ==========================================

df.columns = df.columns.str.strip()

print("\nColumns:", len(df.columns))


# ==========================================
# 4. SEPARATE FEATURES AND LABEL
# ==========================================

X = df.drop(columns=["Label"])
y = df["Label"].astype(str).str.strip()


# ==========================================
# 5. CLEAN FEATURE VALUES
# ==========================================

print("\nCleaning feature values...")

# Convert every feature to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Replace infinity values
X = X.replace([np.inf, -np.inf], np.nan)

# Fill missing numeric values with median
X = X.fillna(X.median())

print("Missing values after cleaning:", X.isnull().sum().sum())


# ==========================================
# 6. ENCODE LABELS
# ==========================================

print("\nEncoding attack labels...")

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

print("\nClasses:")

for number, label in enumerate(label_encoder.classes_):
    print(number, "=", label)


# ==========================================
# 7. TRAIN / TEST SPLIT
# ==========================================

print("\nCreating train/test split...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y_encoded
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 8. CREATE RANDOM FOREST
# ==========================================

print("\nCreating Random Forest model...")

model = RandomForestClassifier(
    n_estimators=150,
    random_state=RANDOM_STATE,
    n_jobs=-1,
    class_weight="balanced_subsample",
    max_features="sqrt"
)


# ==========================================
# 9. TRAIN MODEL
# ==========================================

print("\nTraining model...")
print("This may take some time...\n")

model.fit(X_train, y_train)

print("Training completed!")


# ==========================================
# 10. PREDICTIONS
# ==========================================

print("\nMaking predictions...")

y_pred = model.predict(X_test)


# ==========================================
# 11. EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==========================================")
print("MODEL RESULTS")
print("==========================================")

print("\nAccuracy:", round(accuracy * 100, 2), "%")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_,
        zero_division=0
    )
)


# ==========================================
# 12. CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# ==========================================
# 13. SAVE MODEL
# ==========================================

os.makedirs("models", exist_ok=True)

joblib.dump(model, MODEL_PATH)
joblib.dump(label_encoder, ENCODER_PATH)
joblib.dump(list(X.columns), FEATURES_PATH)

print("\n==========================================")
print("FILES SAVED")
print("==========================================")

print("Model:", MODEL_PATH)
print("Label encoder:", ENCODER_PATH)
print("Feature names:", FEATURES_PATH)

print("\nTraining finished successfully!")