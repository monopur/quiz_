import sqlite3

with open("db/schema.sql") as f:
    schema = f.read()

con = sqlite3.connect("db/quiz.db")
cur = con.cursor()
cur.executescript(schema)
con.commit()
con.close()
print("Veritabanı ve tablolar oluşturuldu.")
