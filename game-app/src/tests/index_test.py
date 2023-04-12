import unittest
import pygame
from index import MySokoban


class TestMySokoban(unittest.TestCase):
    def setUp(self):
        print("Hello")

    def test_set_caption(self):
        pygame.init()
        name = pygame.display.set_caption("My Sokoban")
    
        self.assertEquals(name, "My Sokoban")

    