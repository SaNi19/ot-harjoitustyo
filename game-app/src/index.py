import pygame


class MySokoban:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MySokoban")

        self.images()
        self.game()

        self.height = len(self.map)
        self.width = len(self.map[1])
        self.part = self.images[1].get_width()

        gamemap_height = self.part * self.height
        gamemap_width = self.part * self.width
        self.sreen = pygame.display.set_mode(
            (gamemap_width, gamemap_height + self.part))

        self.loop()

    def images(self):
        self.images = []
        for name in ["floor", "wall", "place", "ball", "player", "end", "player2"]:
            self.images.append(pygame.image.load(name + ".png"))

    def game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
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
                    exit()
            if command.type == pygame.QUIT:
                exit()

    def move(self, move_y, move_x):
        if self.game_done():
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
                    self.images[square], (row * self.part, column * self.part))

        pygame.display.flip()

    def game_done(self):
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
