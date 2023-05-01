class ResultsService:
    """Luokka, joka vastaa tiedon tallentamisesta ja etsimisestä.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo pelaajalistan.
        """
        self.__players = {}

    def add_result(self, name: str, game_result: int):
        """Tallentaa pelaajan tuloksen. Jos pelaajalla ei ole
        vielä tulosta, luo pelaajalle uuden tuloslistan.

        Args:
            name (str): pelaajan nimi
            game_result (int): pelissä käytetyt askeleet
        """
        if not name in self.__players:
            self.__players[name] = []

        self.__players[name].append(game_result)

    def get_result(self, name: str):
        """Etsii nimeä vastaavat tulokset tuloslistasta.

        Args:
            name (str): pelaajan nimi

        Returns:
            List: Palauttaa pelaajan tuloslistan.
            None: Jos pelaajan nimeä vastaavia tuloksia ei löydy,
            palauttaa None.
        """
        if not name in self.__players:
            return None

        return self.__players[name]

    def all_results(self):
        """Palauttaa listan kaikista pelaajista ja tuloksista.

        Returns:
            List: Vieruslistaesitys.
        """
        return self.__players
