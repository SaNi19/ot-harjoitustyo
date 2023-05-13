import sqlite3


class GameServices:
    """Luokka, jonka avulla tulos tallennetaan tietokantaa
    ja etsitään tulos, jossa on käytetty vähiten askeleita.
    """

    def __init__(self, get_result):
        """Luokan kostruktori, joka luo uuden tuloksen.

        Args:
            get_result: Pelissä käytetyt askeleet.
        """
        self.data = sqlite3.connect("resultlist.db")
        self.get_result = get_result
        self.data.isolation_level = None
        """Tarkistaa, onko tietokanta jo luotu. Jos tietokanta on valmiina,
        palauttaa teksitn "Table is created".
        """
        try:
            self.data.execute(
                "CREATE TABLE Resultlist (id INTEGER PRIMARY KEY, name TEXT, result INTEGER)")
        except:
            print("Table is created")

    def add_game_result(self, user_name, game_result):
        """Lisäää pelaajan nimen ja pelissä käytetyt askeleet tietokantaan.

        Args:
            user_name: Käyttäjän nimi.
            game_result: Pelissä käytetyt askeleet.
        """
        name = user_name
        result = game_result
        self.data.execute(
            "INSERT INTO Resultlist (name, result) VALUES (?,?)", [name, result])

    def best_result(self):
        """Etsii pelattujen pelien tuloksen, jossa on käytetty vähiten askeleita.
        Jos tietokannasta löytyy tulos, palauttaa tuloksen. 
        Jos vielä ei ole tuloksia, palauttaa viestin "No results yet"

        """
        best = self.data.execute(
            "SELECT MIN(result) FROM Resultlist").fetchone()
        if best:
            print("Best result now is ", best)
        else:
            print("No results yet")
