import mysql.connector
import pandas as pd

# Database connection
conn=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="",
        db="my_streamlit"

    )

c= conn.cursor()

# Query data
query = "SELECT * FROM customers;"
df = pd.read_sql(query, conn)

# Save to CSV
df.to_csv("dataset.csv", index=False)

print("Data exported to dataset.csv successfully!")
