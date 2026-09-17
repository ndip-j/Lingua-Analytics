import pandas as pd
import sqlite3

df = pd.read_csv("cleaned_transcripts.csv")

conn = sqlite3.connect("linguaspan_analytics.db")

df.to_sql(
    "transcripts",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully.")

conn.close()