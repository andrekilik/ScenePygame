import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
