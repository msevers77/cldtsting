import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Replace with your real values
DB_USER = 'postgres'
DB_PASSWORD = 'cnDlb10n&'
DB_HOST = 'cldtstdb.c78c0w2g01os.eu-north-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'postgres'

# Create the connection string
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Optional: Create the table if it doesn't exist
from sqlalchemy import text
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            full_name TEXT NOT NULL,
            state TEXT NOT NULL
        )
    """))
    conn.commit()  # commit the transaction

# Simulate loading from a CSV
df = pd.DataFrame({
    'full_name': ['Alice Smith', 'Bob Johnson', 'Carlos Reyes'],
    'state': ['CA', 'NY', 'TX']
})

# Load the data into the database
df.to_sql('customers', engine, if_exists='append', index=False)

print("✅ Customer data loaded!")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM customers"))
    for row in result:
        print(row)