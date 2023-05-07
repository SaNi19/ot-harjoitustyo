import sys
import os
import pygame


class MySokoban:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MySokoban")
        self.dirname = os.path.dirname(__file__)

        self.images()
        self.game()

        self.height = len(self.map)
        self.width = len(self.map[1])
        self.part = self.imageset[0].get_width()
        gamemap_height = self.part * self.height
        gamemap_width = self.part * self.width
        self.sreen = pygame.display.set_mode(
            (gamemap_width, gamemap_height + self.part))
        self.fontti = pygame.font.SysFont("Corbel", 30)

        self.loop()

    def images(self):
        self.imageset = []
        for name in ["floor", "wall", "place", "ball", "player", "end", "player2"]:
            self.imageset.append(pygame.image.load(
                os.path.join(self.dirname, "images", name + ".png")))

    def game(self):
        self.step = 0
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 3, 1, 0, 3, 0, 0, 3, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1, 3, 1, 1, 3, 3, 0, 1, 2, 2, 2, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
                    [1, 0, 3, 0, 3, 1, 3, 0, 1, 1, 1, 1, 0, 0, 2, 1],
                    [1, 0, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def events(self):
        for command in pygame.event.get():
            if command.type == pygame.KEYDOWN:
                if command.key == pygame.K_LEFT:
                    self.move(0, -1)
                if command.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if command.key == pygame.K_UP:
                    self.move(-1, 0)
                if command.key == pygame.K_DOWN:
                    self.move(1, 0)
                if command.key == pygame.K_ESCAPE:
                    sys.exit()
                if command.key == pygame.K_F2:
                    self.game()
            if command.type == pygame.QUIT:
                sys.exit()

    def move(self, move_y, move_x):
        if self.game_end():
            return

        old_player_y, old_player_x = self.find()
        new_player_y = old_player_y + move_y
        new_player_x = old_player_x + move_x

        if self.map[new_player_y][new_player_x] == 1:
            return

        if self.map[new_player_y][new_player_x] in [3, 5]:
            new_ball_y = new_player_y + move_y
            new_ball_x = new_player_x + move_x

            if self.map[new_ball_y][new_ball_x] in [1, 3, 5]:
                return

            self.map[new_player_y][new_player_x] -= 3
            self.map[new_ball_y][new_ball_x] += 3

        self.map[old_player_y][old_player_x] -= 4
        self.map[new_player_y][new_player_x] += 4
        self.step += 1

    def find(self):
        for column in range(self.height):
            for row in range(self.width):
                if self.map[column][row] in [4, 6]:
                    return (column, row)

    def display_game(self):
        self.sreen.fill((100, 0, 255))

        for column in range(self.height):
            for row in range(self.width):
                square = self.map[column][row]
                self.sreen.blit(
                    self.imageset[square], (row * self.part, column * self.part))
        tekst = self.fontti.render("Step: " + str(self.step), True, (0, 0, 0))
        self.sreen.blit(tekst, (25, self.height * self.part + 10))

        tekst = self.fontti.render("New game: F2", True, (0, 0, 0))
        self.sreen.blit(tekst, (330, self.height * self.part + 10))

        tekst = self.fontti.render("Close: esc", True, (0, 0, 0))
        self.sreen.blit(tekst, (680, self.height * self.part + 10))

        if self.game_end():
            tekst = self.fontti.render(
                "Game over! All right!", True, (255, 0, 0))
            tekst_x = self.part * self.width / 2 - tekst.get_width() / 2
            tekst_y = self.part * self.height / 2 - tekst.get_height() / 2
            pygame.draw.rect(self.sreen, (0, 0, 0), (tekst_x,
                             tekst_y, tekst.get_width(), tekst.get_height()))
            self.sreen.blit(tekst, (tekst_x, tekst_y))

        pygame.display.flip()

    def game_end(self):
        for column in range(self.height):
            for row in range(self.width):
                if self.map[column][row] in [2, 6]:
                    return False

        return True

    def loop(self):
        while True:
            self.events()
            self.display_game()


if __name__ == "__main__":
    MySokoban()
