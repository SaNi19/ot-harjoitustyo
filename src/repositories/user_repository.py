import os

class UserRepository:
    def __init__(self, data):
        self.__data = data

    def load(self):
        usernames = {}
        with open(self.__data) as f:
            for row in f:
                bit = row.strip().split(':')
                username, * name = bit
                usernames[username] = name


            return usernames

