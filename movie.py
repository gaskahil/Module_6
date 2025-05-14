import sqlite3
from pprint import pp

# Connect to the database
con = sqlite3.connect("movie_database.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

# Insert data
cur.execute("""
  INSERT INTO movies (title, release_year, genre)
  VALUES ("Inception", 2010, "Science Fiction")
""")
con.commit()

# Fetch data
cur.execute("SELECT * FROM movies")
rows = cur.fetchall()

# Display results
pp([dict(row) for row in rows])
pp(rows[0]['title'])
