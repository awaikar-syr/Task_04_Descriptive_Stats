import pandas as pd

# Load the dataset
file_path = '2024_tw_posts_president_scored_anon.csv'
df = pd.read_csv(file_path)

print("\n=== OVERALL DATASET STATISTICS ===")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

for col in df.columns:
    print(f"\nColumn: {col}")
    col_data = df[col]
    non_empty = col_data.dropna()
    print(f"  Count: {len(col_data)}")
    print(f"  Non-empty: {len(non_empty)}")
    if pd.api.types.is_numeric_dtype(col_data):
        print(f"  Type: Numeric")
        print(f"  Mean: {non_empty.mean():.2f}")
        print(f"  Min: {non_empty.min()}")
        print(f"  Max: {non_empty.max()}")
        print(f"  Std: {non_empty.std():.2f}")
        print(f"  Unique values: {non_empty.nunique()}")
    else:
        print(f"  Type: Categorical")
        print(f"  Unique values: {non_empty.nunique()}")
        most_common = non_empty.value_counts().head(5)
        print(f"  Most frequent values:")
        for value, count in most_common.items():
            percent = (count / len(non_empty)) * 100 if len(non_empty) else 0
            print(f"    '{value}': {count} times ({percent:.1f}%)")

# --- GROUPED ANALYSIS BY 'source' ---
if 'source' in df.columns:
    print("\n=== GROUPED ANALYSIS BY 'source' ===")
    for source, group in df.groupby('source'):
        print(f"\n--- source: {source} (n={len(group)}) ---")
        for col in group.columns:
            print(f"  Column: {col}")
            col_data = group[col]
            non_empty = col_data.dropna()
            print(f"    Count: {len(col_data)}")
            print(f"    Non-empty: {len(non_empty)}")
            if pd.api.types.is_numeric_dtype(col_data):
                print(f"    Type: Numeric")
                print(f"    Mean: {non_empty.mean():.2f}")
                print(f"    Min: {non_empty.min()}")
                print(f"    Max: {non_empty.max()}")
                print(f"    Std: {non_empty.std():.2f}")
                print(f"    Unique values: {non_empty.nunique()}")
            else:
                print(f"    Type: Categorical")
                print(f"    Unique values: {non_empty.nunique()}")
                most_common = non_empty.value_counts().head(5)
                print(f"    Most frequent values:")
                for value, count in most_common.items():
                    percent = (count / len(non_empty)) * 100 if len(non_empty) else 0
                    print(f"      '{value}': {count} times ({percent:.1f}%)")
