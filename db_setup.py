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

# cur.execute("CREATE TABLE IF NOT EXISTS Highscores(scores INTEGER)")


def display_highscores():
    "displays the highscores in a row format"
    rows = ""
    cur.execute("SELECT * FROM Highscores ORDER BY scores ASC")
    for row in cur.fetchall():
        rows += str(row[0]) + "\n"
    return rows


winners_score = int(input("num pls: "))


def insert_winners_score(int) -> int:
    "Inserts the winners score if it is valid"
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


insert_winners_score(winners_score)
print(display_highscores())


con.close()