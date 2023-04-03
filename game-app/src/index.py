import pygame
class Sokoban:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sokoban")

        self.load_images()
        self.game()
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.part = self.images[0].get_width()

        gamemap_height = self.part * self.height
        gamemap_width = self.part * self.width
        self.sreen = pygame.display.set_mode((gamemap_width, gamemap_height))

        self.loop()

    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "pallo", "maali", "otus"]:
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
        
    def loop(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()

    def piirra_naytto(self):
        self.sreen.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                bit = self.map[y][x]
                self.sreen.blit(self.images[bit], (x * self.part, y * self.part))

        pygame.display.flip()

if __name__ == "__main__":
    Sokoban()