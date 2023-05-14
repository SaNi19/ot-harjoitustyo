import unittest
import sqlite3
from game_services import GameServices


class TestMySokoban(unittest.TestCase):
    def setUp(self):
        self.game_services = GameServices

        self.data = sqlite3.connect("resultlist.db")
        get_result = 500
        self.get_result = get_result
        self.data.isolation_level = None

    def test_best_result_equal(self):
        answer = self.game_services.best_result(self)

        self.assertEqual(str(answer), "19")

    def test_set_result_equal(self):
        self.game_services.add_game_result(self, 18)
        answer = self.game_services.best_result(self)

        self.assertEqual(str(answer), "18")
