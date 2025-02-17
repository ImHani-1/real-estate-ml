import pandas as pd

# Load the Excel file
excel_file = '../abha_2022q1_2023q1_q2_q3.xlsx'

# Load all sheets
xls = pd.ExcelFile(excel_file)

# Show all sheet names
print("Sheet Names:", xls.sheet_names)

# Load the first sheet (you can change the sheet name or index)
df = pd.read_excel(xls, sheet_name=0)

# Show first few rows to inspect
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Extract unique values for each column
for column in df.columns:
    unique_values = df[column].dropna().unique()
    print(f"\nUnique values in '{column}':")
    print(unique_values)
