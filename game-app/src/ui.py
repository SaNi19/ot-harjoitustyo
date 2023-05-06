
import sqlite3
from index import MySokoban

class UI:
    def __init__(self): 
        self.db = sqlite3.connect("resultlist.db")
        self.db.isolation_level = None
        try:
            self.db.execute("CREATE TABLE Resultlist (id INTEGER PRIMARY KEY, name TEXT, result INTEGER)")
        except:
            print("Taulua ei voitu luoda")


    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add result")
        print("2 find result")
        print("3 best result")

    def run(self):
        self.help()
        while True:
            print("")
            command = input("commands: ")
            if command == "0":
                self.end_app()
                break
            elif command == "1":
                self.add_game_result()
            elif command == "2":
                self.get_result()
            elif command == "3":
                self.best_result()
            elif command == "4":
                self.start()
           
        
    def add_game_result(self):
        name = input("name: ")
        result = input("result: ")  
        self.db.execute("INSERT INTO Resultlist (name, result) VALUES (?,?)", [name, result])

    def get_result(self):
        name = input("name: ")
        result = self.db.execute("SELECT MIN(result) FROM Resultlist WHERE name=?", [name]).fetchone()
        if result:
            print("Result is", result[0])
        else:
            print("No results yet")
    
    def best_result(self):
        best = self.db.execute("SELECT MIN(result) FROM Resultlist").fetchone()
        if best:
            print("Best result now is", best)
        else:
            print("No results yet")
    
    def start(self):
        MySokoban()
        
    def end_app(self):
        return None
        

app = UI()
app.run()

