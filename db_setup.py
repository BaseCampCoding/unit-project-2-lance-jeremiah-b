import sqlite3

con = sqlite3.connect("Battleship.db")

cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Ships(name TEXT, length INTEGER, width INTEGER)"
)

cur.execute(
    """INSERT INTO Ships VALUES
    ('Carrier', 5, 1),
    ('Battleship', 4, 1),
    ('Cruiser', 3, 1),
    ('Submarine', 3, 1),
    ('Destroyer', 2, 1)
"""
)
