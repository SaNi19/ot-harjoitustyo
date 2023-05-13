import sqlite3


class GameServices:
    def __init__(self, get_result, start):
        self.data = sqlite3.connect("resultlist.db")
        self.get_result = get_result
        self.start = start
        self.data.isolation_level = None
        try:
            self.data.execute(
                "CREATE TABLE Resultlist (id INTEGER PRIMARY KEY, name TEXT, result INTEGER)")
        except:
            print("Table is created")

    def add_game_result(self, game_result):
        # name = input("name: ")
        name = "player"
        # result = input("result: "
        result = game_result
        self.data.execute(
            "INSERT INTO Resultlist (name, result) VALUES (?,?)", [name, result])

    def best_result(self):
        best = self.data.execute(
            "SELECT MIN(result) FROM Resultlist").fetchone()
        if best:
            print("Best result now is ", best)
        else:
            print("No results yet")
