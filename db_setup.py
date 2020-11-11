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
# con.close()

cur.execute("CREATE TABLE IF NOT EXISTS Highscores(scores INTEGER)")

winners_score = int(input("num pls: "))

highscore_list = []
cur.execute("SELECT * FROM Highscores")
for row in cur.fetchall():
    highscore_list.append(row[0])

if not winners_score in highscore_list:
    cur.execute("INSERT INTO Highscores VALUES (?)", (winners_score,))

cur.execute("SELECT * FROM Highscores")
if len(cur.fetchall()) > 5:
    cur.execute("SELECT * FROM Highscores ORDER BY scores DESC LIMIT 1")
    max_num = cur.fetchall()[0][0]
    cur.execute("DELETE FROM Highscores WHERE scores = ?", (str(max_num),))

con.commit()

cur.execute("SELECT * FROM Highscores")
for row in cur.fetchall():
    print(row[0])

con.close()