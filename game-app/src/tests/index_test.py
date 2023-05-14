import unittest
import sys
import pygame
from index import MySokoban


imageset = ["floor", "wall", "place", "ball", "player", "end", "player2"]

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 4, 0, 0, 0, 0, 1, 1, 0, 1, 1],
       [1, 1, 1, 3, 3, 3, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

part = 50

height = len(map)
width = len(map[1])
gamemap_height = part * height
gamemap_width = part * width


class TestMySokoban(unittest.TestCase):
    def setUp(self):
        self.map = map

    def find(self):
        for column in range(height):
            for row in range(width):
                if self.map[column][row] in [4, 6]:
                    return (column, row)

    def test_assert_coordinates_y_equal(self):
        answer = self.find()

        self.assertEqual(str(answer), "(1, 1)")

    def test_assert_coordinates_x_equal(self):
        old_x = old_player_y, old_player_x = self.find()
        answer = str(old_x)

        self.assertEqual(answer, "(1, 1)")

    def test_imageset_size_is_right(self):
        answer = len(imageset)

        self.assertEqual(str(answer), "7")

    def test_map_size_is_right(self):
        answer = len(map)

        self.assertEqual(str(answer), "5")

    def test_image_size_is_right(self):
        answer = len(map[1])

        self.assertEqual(str(answer), "11")

    def test_game_end(self):
        for column in range(height):
            for row in range(width):
                if self.map[column][row] in [2, 6]:
                    answer = False
                    return answer

        answer = True

        self.assertEqual(str(answer, "False"))

    