import pandas as pd

# Load the Excel file
df = pd.read_excel('../abha_2022q1_2023q1_q2_q3.xlsx')

# Print first 5 rows
print("📊 Preview of Dataset:")
print(df.head())

# Print column names
print("\n🗂️ Columns in Dataset:")
print(df.columns)
