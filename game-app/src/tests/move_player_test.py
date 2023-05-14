import unittest
import sys
import pygame
from move_player import MovePlayer
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
        self.old_player_y, self.old_player_x = (1,1)

    def game_end(self):
        """Tarkistaa, onko palloja vielä pelilaudalla.

            Returns:
                True: Jos pelilaudalla ei ole enään palloja.
                False: Jos pelilaudalta löytyy vielä palloja.
        """
        for column in range(self.height):
            for row in range(self.width):
                if self.map[column][row] in [2, 6]:
                    return False

        return True


    
    def test_player_can_move(self):
        
        ansver = MySokoban.find(self)

        self.assertTrue(str(ansver), "1,1")

