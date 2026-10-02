import pandas as pd
import os

DATASET_PATH = "dataset/MachineLearningCVE"
OUTPUT_PATH = "dataset/cicids_balanced.csv"

MAX_SAMPLES_PER_LABEL = 10000
RANDOM_STATE = 42


# Find CSV files
csv_files = [
    file for file in os.listdir(DATASET_PATH)
    if file.lower().endswith(".csv")
]

print("Found", len(csv_files), "CSV files")


all_parts = []

for file in csv_files:

    path = os.path.join(DATASET_PATH, file)

    print("\nReading:", file)

    df = pd.read_csv(path)

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Clean label text
    df["Label"] = df["Label"].astype(str).str.strip()

    print("Rows:", len(df))

    # Show labels in this file
    print(df["Label"].value_counts())

    # Take maximum 10,000 samples from each label
    for label in df["Label"].unique():

        label_data = df[df["Label"] == label]

        sample_size = min(
            MAX_SAMPLES_PER_LABEL,
            len(label_data)
        )

        sampled = label_data.sample(
            n=sample_size,
            random_state=RANDOM_STATE
        )

        all_parts.append(sampled)


print("\nCombining datasets...")

combined_df = pd.concat(
    all_parts,
    ignore_index=True
)

# Replace infinite values with NaN
combined_df = combined_df.replace(
    [float("inf"), float("-inf")],
    pd.NA
)

# Remove rows containing missing values
before = len(combined_df)

combined_df = combined_df.dropna()

after = len(combined_df)

print("\nRows removed because of missing/infinite values:", before - after)

# Shuffle the final dataset
combined_df = combined_df.sample(
    frac=1,
    random_state=RANDOM_STATE
).reset_index(drop=True)


print("\n========== FINAL DATASET ==========")

print("Rows:", len(combined_df))
print("Columns:", len(combined_df.columns))

print("\nLabels:")
print(combined_df["Label"].value_counts())

# Save
combined_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nSaved to:")
print(OUTPUT_PATH)