from file_manager import FileManager
from results_service import ResultsService


class UI:
    """Luokka, joka vastaa ohjelman käyttöliittymästä
    """

    def __init__(self):
        """Luokan konstruktori, joka luo tuloslistan ja tiedostonhallinnan.
        """
        self.__results_list = ResultsService()
        self.__filemanager = FileManager("data.txt")

        for name, results in self.__filemanager.load().items():
            for steps in results:
                self.__results_list.add_result(name, steps)

    def help(self):
        """Näyttää käyttäjälle ohjelman valikkotoiminnot.
        """
        print("commands: ")
        print("0 exit")
        print("1 add result")
        print("2 find result")
        print("3 all results")

    def run(self):
        """Käynnistää ohjelman valikon ja kutsuu metodeita käyttäjän valinnan mukaan.
        """
        self.help()
        while True:
            print("")
            command = input("commands: ")
            if command == "0":
                self.end_app()
                break
            if command == "1":
                self.add_game_result()
            if command == "2":
                self.get_result()
            if command == "3":
                self.all_result

    def add_game_result(self):
        """Kysyy käyttäjän nimen ja tuloksen, ja tallentaa tuloksen tiedostoon.
        """
        name = input("name: ")
        result = input("result: ")
        self.__results_list.add_result(name, result)

    def get_result(self):
        """Kysyy käyttäjältä nimeä ja hakee tiedostosta nimeä vastaavan tuloslistan.
        Jos nimeä vastaavia tuloksia ei löydy, palauttaa viestin: "No results yet".
        """
        name = input("name: ")
        results = self.__results_list.get_result(name)
        if results is None:
            print("No results yet")
            return
        for reg in results:
            print(reg)

    def all_result(self):
        """Tulostaa listan kaikista pelaajista ja pelaajien tuloksista.
        Jos tuloksia ei löydy, palauttaa viestin: "No results yet".
        Args:
            List: Pelaajat ja tulokset
        """
        all_results = self.__results_list.all_results()
        if all_results is None:
            print("No results yet")
            return

        print(self.__results_list.all_results)

    def end_app(self):
        """Tallentaa kaikki tulokset ja sulkee ohjelman.
        """
        self.__filemanager.save_result(self.__results_list.all_results())


ui = UI()
ui.run()
