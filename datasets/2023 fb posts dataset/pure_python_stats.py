import csv
import math
from collections import Counter

# Load the dataset
file_path = '2024_fb_posts_president_scored_anon.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

# Transpose data to columns
data_by_col = list(zip(*data))

print(f"Total rows: {len(data)}")
print(f"Total columns: {len(header)}")

for col_idx, col_name in enumerate(header):
    col_data = [v.strip() for v in data_by_col[col_idx]]
    non_empty = [v for v in col_data if v]
    print(f"\nColumn: {col_name}")
    print(f"  Count: {len(col_data)}")
    print(f"  Non-empty: {len(non_empty)}")
    # Try to convert to float for numeric analysis
    numeric_vals = []
    for v in non_empty:
        try:
            numeric_vals.append(float(v))
        except ValueError:
            pass
    if numeric_vals and len(numeric_vals) == len(non_empty):
        # Numeric column
        mean = sum(numeric_vals) / len(numeric_vals)
        min_v = min(numeric_vals)
        max_v = max(numeric_vals)
        std = math.sqrt(sum((x - mean) ** 2 for x in numeric_vals) / (len(numeric_vals) - 1)) if len(numeric_vals) > 1 else 0.0
        unique_count = len(set(numeric_vals))
        print(f"  Type: Numeric")
        print(f"  Mean: {mean:.2f}")
        print(f"  Min: {min_v}")
        print(f"  Max: {max_v}")
        print(f"  Std: {std:.2f}")
        print(f"  Unique values: {unique_count}")
    else:
        # Categorical column
        value_counts = Counter(non_empty)
        unique_count = len(value_counts)
        most_common = value_counts.most_common(5)
        print(f"  Type: Categorical")
        print(f"  Unique values: {unique_count}")
        print(f"  Most frequent values:")
        for value, count in most_common:
            percent = (count / len(non_empty)) * 100 if non_empty else 0
            print(f"    '{value}': {count} times ({percent:.1f}%)")

# --- GROUPED ANALYSIS BY 'Facebook_Id' ---
if 'Facebook_Id' in header:
    fb_id_idx = header.index('Facebook_Id')
    groups = {}
    for row in data:
        key = row[fb_id_idx]
        groups.setdefault(key, []).append(row)
    print("\n--- Grouped Analysis by 'Facebook_Id' ---")
    for fb_id, group_rows in groups.items():
        print(f"\n=== Facebook_Id: {fb_id} (n={len(group_rows)}) ===")
        group_cols = list(zip(*group_rows))
        for col_idx, col_name in enumerate(header):
            col_data = [v.strip() for v in group_cols[col_idx]]
            non_empty = [v for v in col_data if v]
            print(f"  Column: {col_name}")
            print(f"    Count: {len(col_data)}")
            print(f"    Non-empty: {len(non_empty)}")
            numeric_vals = []
            for v in non_empty:
                try:
                    numeric_vals.append(float(v))
                except ValueError:
                    pass
            if numeric_vals and len(numeric_vals) == len(non_empty):
                mean = sum(numeric_vals) / len(numeric_vals)
                min_v = min(numeric_vals)
                max_v = max(numeric_vals)
                std = math.sqrt(sum((x - mean) ** 2 for x in numeric_vals) / (len(numeric_vals) - 1)) if len(numeric_vals) > 1 else 0.0
                unique_count = len(set(numeric_vals))
                print(f"    Type: Numeric")
                print(f"    Mean: {mean:.2f}")
                print(f"    Min: {min_v}")
                print(f"    Max: {max_v}")
                print(f"    Std: {std:.2f}")
                print(f"    Unique values: {unique_count}")
            else:
                value_counts = Counter(non_empty)
                unique_count = len(value_counts)
                most_common = value_counts.most_common(5)
                print(f"    Type: Categorical")
                print(f"    Unique values: {unique_count}")
                print(f"    Most frequent values:")
                for value, count in most_common:
                    percent = (count / len(non_empty)) * 100 if non_empty else 0
                    print(f"      '{value}': {count} times ({percent:.1f}%)")
