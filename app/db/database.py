import os
import pandas as pd
import sqlite3
from langchain_community.utilities.sql_database import SQLDatabase

# Get the directory where this file is located
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(DB_DIR, 'cortex.db')
DATABASE_URL = f"sqlite:///{DB_FILE}"
PARQUET_PATH = os.path.join(DB_DIR, 'cortex.parquet')

df = pd.read_parquet(PARQUET_PATH)
if not os.path.exists(DB_FILE):
    connection = sqlite3.connect("cortex.db")
    df.to_sql(name="cortex_data", con=connection)
db = SQLDatabase.from_uri(DATABASE_URL)
