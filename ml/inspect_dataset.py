import pandas as pd
import os

dataset_path = "dataset/MachineLearningCVE"

csv_files = [
    file for file in os.listdir(dataset_path)
    if file.lower().endswith(".csv")
]

print("========== CICIDS2017 DATASET ==========\n")

total_rows = 0  

for file in csv_files:

    path = os.path.join(dataset_path, file)

    print("\nReading:", file)

    df = pd.read_csv(path)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("Labels:")
    print(df[" Label"].value_counts())

    total_rows += len(df)

print("\n========================================")
print("Total rows across all files:", total_rows)
print("Number of CSV files:", len(csv_files))