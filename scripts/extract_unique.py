import pandas as pd
import psycopg2

# 1️⃣ Load the Excel file
excel_file = '../abha_2022q1_2023q1_q2_q3.xlsx'
df = pd.read_excel(excel_file)

# 2️⃣ Connect to Supabase Database
conn = psycopg2.connect(
    host="db.your-supabase-url.supabase.co",
    database="postgres",
    user="postgres",
    password="your-supabase-password"
)
cursor = conn.cursor()

# 3️⃣ Insert Unique Values into Property_Classifications
if 'classification_name' in df.columns:
    unique_classifications = df['classification_name'].dropna().unique()
    for value in unique_classifications:
        cursor.execute("""
            INSERT INTO Property_Classifications (classification_name)
            VALUES (%s)
            ON CONFLICT (classification_name) DO NOTHING;
        """, (value,))
    print(f"✅ Inserted {len(unique_classifications)} Property Classifications")

# 4️⃣ Insert Unique Values into Property_Types
if 'property_type_name' in df.columns:
    unique_types = df['property_type_name'].dropna().unique()
    for value in unique_types:
        cursor.execute("""
            INSERT INTO Property_Types (property_type_name)
            VALUES (%s)
            ON CONFLICT (property_type_name) DO NOTHING;
        """, (value,))
    print(f"✅ Inserted {len(unique_types)} Property Types")

# 5️⃣ Commit and Close
conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted into Supabase.")
