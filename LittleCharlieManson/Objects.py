from random import random, choice
import pygame


# constants
cementArray = ['img/Massa.png', 'img/Massa2.png']
yPosM = ['450', '530']
yPosH = ['370']


class Cement(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()

        self.currentPosition = 0
        self.image = pygame.image.load(cementArray[self.currentPosition]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    def animate(self):
        if self.currentPosition != 1:
            self.currentPosition += 1
        else:
            self.currentPosition = 0

        self.image = pygame.image.load(cementArray[self.currentPosition])


class Manhole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('img/Bueiro.png')
        self.rect = self.image.get_rect()
        self.rect.x = 880
        self.rect.y = int(choice(yPosM)) + 20


class Hydrant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('img/Hidrante.png')
        self.rect = self.image.get_rect()
        self.rect.x = 880
        self.rect.y = int(choice(yPosH))


def createObject(creationRate):
    c = False
    if random() <= creationRate:
        c = True

    return c
