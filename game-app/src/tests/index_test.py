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
    def find(self):
        for column in range(height):
            for row in range(width):
                if self.map[column][row] in [4]:
                    return (column, row)

    def setUp(self):
        self.map = map

    def test_assert_coordinates_y_equal(self):
        old_y = old_player_y, old_player_x = self.find()
        answer = str(old_y)

        self.assertEqual(answer, "(1, 1)")

    def test_assert_coordinates_x_equal(self):
        old_x = old_player_y, old_player_x = self.find()
        answer = str(old_x)

        self.assertEqual(answer, "(1, 1)")


    def test_imageset_size_is_right(self):
        length = len(imageset)
        ansver = str(length)

        self.assertEqual(ansver, "7")

    def test_map_size_is_right(self):
        height = len(map)
        ansver = str(height)

        self.assertEqual(ansver, "5")

    def test_image_size_is_right(self):
        waidh = len(map[1])
        ansver = str(waidh)

        self.assertEqual(ansver, "11")
