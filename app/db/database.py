import os
import pandas as pd
import sqlite3
from langchain_community.utilities.sql_database import SQLDatabase

# Set up file paths for database and data
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(DB_DIR, 'cortex.db')
DATABASE_URL = f"sqlite:///{DB_FILE}"
PARQUET_PATH = os.path.join(DB_DIR, 'cortex.parquet')

# Load data from Parquet file
# If the SQLite DB does not exist, create it from the Parquet data
# This ensures the database is always available for queries
df = pd.read_parquet(PARQUET_PATH)
if not os.path.exists(DB_FILE):
    connection = sqlite3.connect("cortex.db")
    df.to_sql(name="cortex_data", con=connection)
# Create a LangChain SQLDatabase instance for use by tools
# This object is used by the agent tools to run SQL queries
db = SQLDatabase.from_uri(DATABASE_URL)
