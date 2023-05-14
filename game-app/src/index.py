import sys
import os
import sqlite3
import pygame
from game_services import GameServices
from move_player import MovePlayer


class MySokoban:
    """Luokka, joka vastaa pelikentän luomisesta ja pelin toiminnoista.

    """

    def __init__(self):
        self.self = self
        pygame.init()
        pygame.display.set_caption("MySokoban")
        self.dirname = os.path.dirname(__file__)
        self.data = sqlite3.connect("resultlist.db")
        self.move_player = MovePlayer
        self.game_services = GameServices
        self.best = self.game_services.best_result(self)

        self.images()
        """Kutsutaan metodi, joka asettaa image-kansion kuvat taulukkoon.
        """
        self.game()
        """Kutsutaan metodi, joka luo pelilaudan.
        """

        self.height = len(self.map)
        self.width = len(self.map[1])
        self.part = self.imageset[0].get_width()
        gamemap_height = self.part * self.height
        gamemap_width = self.part * self.width
        self.sreen = pygame.display.set_mode(
            (gamemap_width, gamemap_height + self.part))
        self.font1 = pygame.font.SysFont("Corbel", 25)
        self.font2 = pygame.font.SysFont("Corbel", 60)
        self.steps = 0

        self.loop()
        """Kutsutaan pelisilmukkametodia.
        """

    def images(self):
        """Metodi, joka settaa kuvat taulukkoon.
        """
        self.imageset = []
        for name in ["floor", "wall", "place", "ball", "player", "end", "player2"]:
            self.imageset.append(pygame.image.load(
                os.path.join(self.dirname, "images", name + ".png")))

    def game(self):
        """Alustaa pelilaudan.
        """

        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 3, 1, 0, 3, 0, 0, 3, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1, 3, 1, 1, 3, 3, 0, 1, 2, 2, 2, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
                    [1, 0, 3, 0, 3, 1, 3, 0, 1, 1, 1, 1, 0, 0, 2, 1],
                    [1, 0, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.map1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 4, 1, 1, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 3, 0, 1, 1, 0, 1, 1],
                     [1, 0, 3, 0, 0, 1, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 2, 2, 2, 1],
                     [1, 0, 3, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.step = 0
        """Askellaskuri.
            Args:
            step: Askeleet alussa 0.
        """
    def events(self):
        """Tapahtumankäsittelijä.
        """
        for command in pygame.event.get():
            if command.type == pygame.KEYDOWN:
                if command.key == pygame.K_LEFT:
                    self.move_player.move(self, 0, -1)
                if command.key == pygame.K_RIGHT:
                    self.move_player.move(self, 0, 1)
                if command.key == pygame.K_UP:
                    self.move_player.move(self, -1, 0)
                if command.key == pygame.K_DOWN:
                    self.move_player.move(self, 1, 0)
                if command.key == pygame.K_ESCAPE:
                    sys.exit()
                if command.key == pygame.K_F2:
                    self.game()
            if command.type == pygame.QUIT:
                sys.exit()
            if command.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.collidepoint(command.pos):
                    sys.exit()
                if self.new_game_button.collidepoint(command.pos):
                    self.game()

    def find(self):
        """Etsii pelihahmon sijainnin pelilaudalla.

        Returns:
            column: y:n arvo
            row: x:n arvo
        """
        for column in range(self.height):
            for row in range(self.width):
                if self.map[column][row] in [4, 6]:
                    return (column, row)

    def display_game(self):
        """Piirtää pelilaudan.
        """
        self.sreen.fill((100, 0, 255))
        for column in range(self.height):
            for row in range(self.width):
                square = self.map[column][row]
                self.sreen.blit(
                    self.imageset[square], (row * self.part, column * self.part))

        tekst = self.font1.render("Step: " + str(self.step), True, (0, 0, 0))
        self.sreen.blit(tekst, (25, self.height * self.part + 10))

        tekst = self.font1.render(
            "Best result: " + str(self.best), True, (0, 0, 0))
        self.sreen.blit(tekst, (150, self.height * self.part + 10))

        self.new_game_button_text = self.font1.render(
            'New game', True, 'white')
        self.new_game_button = pygame.Rect(
            550, self.height * self.part + 10, 100, 30)

        pygame.draw.rect(self.sreen, (200, 0, 0), self.new_game_button)
        self.sreen.blit(self.new_game_button_text,
                        (self.new_game_button.x + 5, self.new_game_button.y+5))

        self.quit_button_text = self.font1.render('Quit', True, 'white')
        self.quit_button = pygame.Rect(
            700, self.height * self.part + 10, 80, 30)

        pygame.draw.rect(self.sreen, (200, 0, 0), self.quit_button)
        self.sreen.blit(self.quit_button_text,
                        (self.quit_button.x + 5, self.quit_button.y+5))

        if self.game_end():

            """Tarkistaa, onko kaikki pallot varastossa

                Returns:
                    True: Jos kaikki pallot ovat varastossa.
                    False: Jos kaikki pallot eivät ole varastossa.
                    text: Jos kaikki pallot on varastossa, tulostaa 
                    näytölle teksin "Game over! All right!"
            """
            result = self.step
            self.game_services.add_game_result(self, result)
            tekst = self.font1.render(
                "Game over! All right!", True, (255, 0, 0))
            tekst_x = self.part * self.width / 2 - tekst.get_width() / 2
            tekst_y = self.part * self.height / 2 - tekst.get_height() / 2
            pygame.draw.rect(self.sreen, (0, 0, 0), (tekst_x,
                             tekst_y, tekst.get_width(), tekst.get_height()))
            self.sreen.blit(tekst, (tekst_x, tekst_y))

        pygame.display.flip()

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

    def loop(self):
        """Pelisilmukka joka kuuntelee tapahtumia ja piirtää näytön.
        """
        while True:
            self.events()
            self.display_game()


if __name__ == "__main__":
    MySokoban()
