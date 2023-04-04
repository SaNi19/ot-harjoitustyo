import pygame
class MySokoban:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Sokoban")

        self.images()
        self.game()
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.part = self.images[0].get_width()
        gamemap_height = self.part * self.height
        gamemap_width = self.part * self.width
        self.sreen = pygame.display.set_mode((gamemap_width, gamemap_height))

        self.loop()

    def images(self):
        self.images = []
        for name in ["floor", "wall", "ball", "place", "player"]:
            self.images.append(pygame.image.load(name + ".png"))

    def game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 2, 2, 1, 0, 0, 0, 0, 2, 0, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 2, 0, 1, 3, 3, 3, 1],
                    [1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 1],
		            [1, 0, 0, 0, 2, 2, 1, 2, 0, 1, 1, 1, 1, 0, 0, 3, 1],
                    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] 
        
    

    def event(self):
        for command in pygame.event.get():
            if command.type == pygame.QUIT:
                exit()

    def display_game(self):
        self.sreen.fill((0, 0, 0))
        for y in range(self.width):
            for x in range(self.height):
                bit = self.map[x][y]
                self.sreen.blit(self.images[bit], (y * self.part, x * self.part))

        pygame.display.flip()
    
    def loop(self):
        while True:
            self.event()
            self.display_game()

if __name__ == "__main__":
    MySokoban()