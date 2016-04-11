import pygame
from pygame.constants import K_UP, K_DOWN


# constants
baseCharacterMovement = 80
animationArray = ['img/Charlinho.png', 'img/Charlinho2.png', 'img/Charlinho3.png', 'img/Charlinho4.png', 'img/CharlinhoS.png']


class Charlinho(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.currentPosition = 0
        self.image = pygame.image.load(animationArray[self.currentPosition]).convert_alpha()
        self.anmUpdate = 1
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 490

    def move(self, key, hitBox):
        if key == K_UP:
            if self.rect.y != 330:
                self.rect.y -= baseCharacterMovement
        elif key == K_DOWN:
            if self.rect.y != 490:
                self.rect.y += baseCharacterMovement

        hitBox.rect.y = self.rect.y + 60

    def animate(self, cements):
        if self.anmUpdate % 3 == 0:
            self.anmUpdate = 1
            if self.currentPosition != 3:
                self.currentPosition += 1
            else:
                self.currentPosition = 0

            self.image = pygame.image.load(animationArray[self.currentPosition]).convert_alpha()

            for cement in cements:
                cement.animate()
        else:
            self.anmUpdate += 1

    def shoot(self):
        self.image = pygame.image.load(animationArray[4]).convert_alpha()
        self.anmUpdate = 1


class CharlinhoHitBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('img/CharlinhoHitBox.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
