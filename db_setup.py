import sqlite3

con = sqlite3.connect("Battleship.db")

cur = con.cursor()

# cur.execute(
#     "CREATE TABLE IF NOT EXISTS Ships(name TEXT, length INTEGER, width INTEGER)"
# )

# cur.execute(
#     """INSERT INTO Ships VALUES
#     ('Carrier', 5, 1),
#     ('Battleship', 4, 1),
#     ('Cruiser', 3, 1),
#     ('Submarine', 3, 1),
#     ('Destroyer', 2, 1)
# """
# )

cur.execute("CREATE TABLE IF NOT EXISTS Highscores(scores INTEGER)")

winners_score = [5, 4, 5, 9, 6, 2]

for num in winners_score:
    cur.execute("INSERT INTO Highscores VALUES (?)", str(num))

cur.execute("SELECT * FROM Highscores")
for row in cur.fetchall():
    print(row[0])

con.close()