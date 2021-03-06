import sqlite3

def db_highscore_init():
    con = sqlite3.connect("Battleship.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Highscores(scores INTEGER)")
    return con, cur


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


def reset_highscores():  # for debugging purposes
    "Resets highscores"
    con, cur = db_highscore_init()
    cur.execute("DELETE FROM Highscores")
    cur.execute("""INSERT INTO Highscores VALUES
    (101),
    (102),
    (103),
    (104),
    (105)
    """)
    con.commit()


def display_highscore(index):
    """displays the highscore based off the index up to 5
    >>> display_highscore(0)
    15
    """
    con, cur = db_highscore_init()
    cur.execute("SELECT * FROM Highscores ORDER BY scores ASC")
    return cur.fetchall()[index][0]


def insert_winners_score(score: int) -> int:
    """Inserts the winners score if it is valid
    >>> insert_winners_score(10)
    10
    15
    20
    25
    30
    """
    con, cur = db_highscore_init()
    # checks highscore_list to make sure that scores are unique
    highscore_list = []
    cur.execute("SELECT * FROM Highscores")
    for row in cur.fetchall():
        highscore_list.append(row[0])
    if not score in highscore_list:
        cur.execute("INSERT INTO Highscores VALUES (?)", (score,))
    # makes sure that only the top 5 highscores in the table.
    # The table will then update the highscore with the lowest moves made, and delete the highest moves made.
    cur.execute("SELECT * FROM Highscores")
    if len(cur.fetchall()) > 5:
        cur.execute("SELECT * FROM Highscores ORDER BY scores DESC LIMIT 1")
        max_num = cur.fetchall()[0][0]
        cur.execute("DELETE FROM Highscores WHERE scores = ?", (str(max_num),))
    con.commit()

if __name__ == "__main__":
    reset_highscores()
    print(display_highscore(0))