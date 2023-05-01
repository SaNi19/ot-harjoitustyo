class ResultsService:
    def __init__(self):
        self.__players = {}

    def add_result(self, name: str, game_result: int):
        if not name in self.__players:
            self.__players[name] = []

        self.__players[name].append(game_result)

    def get_result(self, name: str):
        if not name in self.__players:
            return None

        return self.__players[name]

    def all_results(self):
        return self.__players
    