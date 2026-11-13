
import pandas as pd
import numpy as np
import joblib
import os

# Load the exact feature names used by the trained model
features = joblib.load("models/feature_names.pkl")

np.random.seed(42)

def create_samples(filename, rows):
    data = {}

    for feature in features:
        name = feature.lower()

        if "port" in name:
            data[feature] = np.random.randint(1, 65535, rows)
        elif "protocol" in name:
            data[feature] = np.random.choice([6, 17], rows)
        elif "flag" in name:
            data[feature] = np.random.randint(0, 5, rows)
        elif "rate" in name or "length" in name or "bytes" in name:
            data[feature] = np.random.uniform(1, 1000, rows)
        else:
            data[feature] = np.random.uniform(0, 100, rows)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Created: {filename}")

os.makedirs("test_data", exist_ok=True)

create_samples("test_data/new_benign_test.csv", 10)
create_samples("test_data/new_attack_test.csv", 10)
