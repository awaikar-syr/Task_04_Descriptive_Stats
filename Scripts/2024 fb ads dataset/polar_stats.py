import polars as pl

# Load the dataset
file_path = '2024_fb_ads_president_scored_anon.csv'
df = pl.read_csv(file_path)

print("\n=== OVERALL DATASET STATISTICS ===")
print(f"Total rows: {df.height}")
print(f"Total columns: {len(df.columns)}")

for col, dtype in zip(df.columns, df.dtypes):
    col_data = df[col]
    non_empty = col_data.drop_nulls()
    print(f"\nColumn: {col}")
    print(f"  Count: {col_data.len()}")
    print(f"  Non-empty: {non_empty.len()}")
    if dtype in [pl.Int64, pl.Float64, pl.Int32, pl.Float32]:
        print(f"  Type: Numeric")
        print(f"  Mean: {non_empty.mean():.2f}")
        print(f"  Min: {non_empty.min()}")
        print(f"  Max: {non_empty.max()}")
        print(f"  Std: {non_empty.std():.2f}")
        print(f"  Unique values: {non_empty.n_unique()}")
    else:
        print(f"  Type: Categorical")
        print(f"  Unique values: {non_empty.n_unique()}")
        most_common = non_empty.value_counts().sort('counts', descending=True).head(5)
        print(f"  Most frequent values:")
        for row in most_common.iter_rows():
            value, count = row[0], row[1]
            percent = (count / non_empty.len()) * 100 if non_empty.len() else 0
            print(f"    '{value}': {count} times ({percent:.1f}%)")

# --- GROUPED ANALYSIS BY 'page_id' ---
if 'page_id' in df.columns:
    print("\n=== GROUPED ANALYSIS BY 'page_id' ===")
    for page_id, group in df.groupby('page_id'):
        print(f"\n--- page_id: {page_id} (n={group.height}) ---")
        for col, dtype in zip(group.columns, group.dtypes):
            col_data = group[col]
            non_empty = col_data.drop_nulls()
            print(f"  Column: {col}")
            print(f"    Count: {col_data.len()}")
            print(f"    Non-empty: {non_empty.len()}")
            if dtype in [pl.Int64, pl.Float64, pl.Int32, pl.Float32]:
                print(f"    Type: Numeric")
                print(f"    Mean: {non_empty.mean():.2f}")
                print(f"    Min: {non_empty.min()}")
                print(f"    Max: {non_empty.max()}")
                print(f"    Std: {non_empty.std():.2f}")
                print(f"    Unique values: {non_empty.n_unique()}")
            else:
                print(f"    Type: Categorical")
                print(f"    Unique values: {non_empty.n_unique()}")
                most_common = non_empty.value_counts().sort('counts', descending=True).head(5)
                print(f"    Most frequent values:")
                for row in most_common.iter_rows():
                    value, count = row[0], row[1]
                    percent = (count / non_empty.len()) * 100 if non_empty.len() else 0
                    print(f"      '{value}': {count} times ({percent:.1f}%)")
