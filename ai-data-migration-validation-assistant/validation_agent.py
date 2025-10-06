import pandas as pd
import json

# Load source and target data
source = pd.read_csv("sample_data/customers_source.csv")
target = pd.read_csv("sample_data/customers_target.csv")

# Step 1: Schema comparison
missing_in_target = list(set(source.columns) - set(target.columns))
extra_in_target = list(set(target.columns) - set(source.columns))

# Step 2: Row count check
source_rows = len(source)
target_rows = len(target)

# Step 3: Value comparison (for matching columns)
common_cols = list(set(source.columns).intersection(set(target.columns)))
mismatch_rows = 0
for col in common_cols:
    diff = (source[col] != target[col]).sum()
    mismatch_rows += diff

# Step 4: Prepare validation report
validation_report = {
    "missing_columns": missing_in_target,
    "extra_columns": extra_in_target,
    "source_row_count": source_rows,
    "target_row_count": target_rows,
    "row_difference": abs(source_rows - target_rows),
    "mismatched_values": mismatch_rows,
    "overall_accuracy": round((1 - mismatch_rows / source_rows) * 100, 2)
}

# Save JSON report
with open("output/validation_summary.txt", "w") as f:
    f.write(json.dumps(validation_report, indent=2))

print("Validation completed! Summary saved to output/validation_summary.txt")

# Mock AI-generated explanation (like Bedrock output)
ai_summary = f"""
Migration Validation Summary
============================
✅ Source Rows: {source_rows}, Target Rows: {target_rows}
⚠️ Missing Columns: {missing_in_target if missing_in_target else 'None'}
⚠️ Extra Columns: {extra_in_target if extra_in_target else 'None'}
❗ Value Mismatches: {mismatch_rows} cells differ in shared columns.
✅ Overall Accuracy: {validation_report['overall_accuracy']}%

Recommendation: Verify ETL mapping for missing fields and mismatched region values.
"""
print(ai_summary)
