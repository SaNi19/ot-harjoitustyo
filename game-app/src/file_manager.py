class FileManager():
    """Luokka, joka vastaa tiedostonhallinnasta.
    """

    def __init__(self, data):
        """Luokan konstruktori, joka luo yhteyden tiedostoon data.txt.

        Args:
            data (txt): data.txt
        """
        self.__data = data

    def load(self):
        """Lukee tiedostoa.

        Returns:
            List: Palaajat ja tulokset.
        """
        names = {}
        with open(self.__data) as file:
            for row in file:
                parts = row.strip().split(';')
                name, *results_list = parts
                names[name] = results_list

        return names

    def save_result(self, data: dict):
        """Kirjoittaa tiedostoon.

        Args:
            data (dict): Pelaajan nimi ja tulos.
        """
        with open(self.__data, "w") as file:
            for name, results in data.items():
                row = [name] + results
                file.write(";".join(row) + "\n")
