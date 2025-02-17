import pandas as pd

# Load Excel file
df = pd.read_excel('../data/abha_2022.xlsx')

# Extract unique values
regions = df['المنطقة'].unique()
cities = df['المدينة'].unique()
neighborhoods = df['الحي'].unique()
classifications = df['تصنيف العقار'].unique()
property_types = df['نوع العقار'].unique()

# Save to CSV
pd.Series(regions).to_csv('../data/unique_regions.csv', index=False)
pd.Series(cities).to_csv('../data/unique_cities.csv', index=False)
pd.Series(neighborhoods).to_csv('../data/unique_neighborhoods.csv', index=False)
pd.Series(classifications).to_csv('../data/unique_classifications.csv', index=False)
pd.Series(property_types).to_csv('../data/unique_property_types.csv', index=False)

print("Unique values extracted successfully!")
