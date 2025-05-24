import sqlite3
import os

schema_path = os.path.join(os.path.dirname(__file__), "db", "schema.sql")
db_path = os.path.join(os.path.dirname(__file__), "db", "quiz.db")

with open(schema_path) as f:
    schema = f.read()

con = sqlite3.connect(db_path)
cur = con.cursor()
cur.executescript(schema)
con.commit()
con.close()
print("Veritabanı ve tablolar güncellendi.")
