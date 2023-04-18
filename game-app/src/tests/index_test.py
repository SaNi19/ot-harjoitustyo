import unittest
import pygame

from index import MySokoban

imageset = ["floor", "wall", "place", "ball", "player", "end", "player2"]

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 3, 1, 0, 3, 0, 0, 3, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1, 3, 1, 1, 3, 3, 0, 1, 2, 2, 2, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
                    [1, 0, 3, 0, 3, 1, 3, 0, 1, 1, 1, 1, 0, 0, 2, 1],
                    [1, 0, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class TestMySokoban(unittest.TestCase):

    

    def test_imageset_size_is_right(self):
        length = len(imageset)
        ansver = str(length)

        self.assertEqual(ansver, "7")

    def test_map_size_is_right(self):
        height = len(map)
        ansver =str(height)

        self.assertEqual(ansver, "8")

    def test_image_size_is_right(self):
        part = len(map[1])
        ansver =str(part)

        self.assertEqual(ansver, "16")


        

        
    
