from file_manager import FileManager
from results_service import ResultsService


class UI:
    def __init__(self):
        self.__results_list = ResultsService()
        self.__filemanager = FileManager("data.txt")

        for name, results in self.__filemanager.load().items():
            for steps in results:
                self.__results_list.add_result(name, steps)


    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add result")
        print("2 find result")
        print("3 all results")

    def run(self):
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
        name = input("name: ")
        result = input("result: ")
        self.__results_list.add_result(name, result)

    def get_result(self):
        name = input("name: ")
        results = self.__results_list.get_result(name)
        if results is None:
            print("No aresults yet")
            return
        for reg in results:
            print(reg)

    def all_result(self):
        all_results = self.__results_list.all_results()
        if all_results is None:
            print("No results yet")
            return

        print(self.__results_list.all_results)

    def end_app(self):
        self.__filemanager.save_result(self.__results_list.all_results())



app = UI()
app.run()
