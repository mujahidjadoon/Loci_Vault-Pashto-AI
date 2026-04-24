import pandas as pd
import os

# Ab humne naam asaan kar dia hai
input_file = "scripts/data.parquet"
output_file = "scripts/Pashto_Data_Ready.csv"

if os.path.exists(input_file):
    print("🚀 File mil gayi! M4 Power se conversion shuru...")
    # Parquet parhain
    df = pd.read_parquet(input_file)

    # CSV mein save karein
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"✅ Mubarak ho! '{output_file}' ban gayi hai.")
else:
    # Agar ab bhi na mile toh ye print karega ke terminal abhi kahan khara hai
    print(f"❌ Error: '{input_file}' abhi bhi nahi mili.")
    print(f"🔍 Current Folder: {os.getcwd()}")