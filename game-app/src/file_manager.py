class FileManager():
    def __init__(self, data):
        self.__data = data

    def load(self):
        names = {}
        with open(self.__data) as file:
            for row in file:
                parts = row.strip().split(';')
                name, *results_list = parts
                names[name] = results_list

        return names

    def save_result(self, data: dict):
        with open(self.__data, "w") as file:
            for name, results in data.items():
                row = [name] + results
                file.write(";".join(row) + "\n")
