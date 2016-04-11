import pygame
from pygame.locals import *
import Objects
from Character import Charlinho, CharlinhoHitBox
from Objects import Cement, Hydrant, Manhole
from random import choice
from Scenario import Element


class LCM_Main:
    def __init__(self):
        pygame.init()

        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Little Charlie Manson')

    def MainLoop(self):
        # Scenario Sprites
        backScenarioGroup = pygame.sprite.Group()
        frontScenarioGroup = pygame.sprite.Group()

        rua = Element('img/rua.png', 1, 1)
        grama = Element('img/grama1.png', 1, 1)
        gramado = Element('img/gramado.png', 1, 1)
        faixaCalcada = Element('img/faixascalcada.png', 1, 1)
        faixaRua = Element('img/faixasrua.png', 1, 1)
        nuvens = Element('img/nuvens.png', 1, 1)
        nuvens2 = Element('img/nuvens.png', 1, 1)
        sol = Element('img/sol1.png', 1, 1)

        backScenarioGroup.add(gramado)
        backScenarioGroup.add(rua)
        backScenarioGroup.add(nuvens)
        backScenarioGroup.add(sol)

        frontScenarioGroup.add(faixaCalcada)
        frontScenarioGroup.add(faixaRua)
        frontScenarioGroup.add(grama)

        # sky's color
        sky = (0, 152, 248)

        # Animation Direction
        direction = 'left'

        player = Charlinho()
        playerHB = CharlinhoHitBox(player.rect.x, player.rect.y+60)

        cements = []
        hydrants = []
        manholes = []
        objects = ['H', 'B']

        allObjGroup = pygame.sprite.Group()
        collGroup = pygame.sprite.Group()

        done = False
        while not done:
            # Scene Animation
            if direction == 'left':
                nuvens.rect.x -= 5
                grama.rect.x -= 5
                if -900 > nuvens.rect.x < -800:
                    direction = 'right'
            elif direction == 'right':
                nuvens.rect.x = 800
                grama.rect.x = 0
                if nuvens.rect.x == 800:
                    direction = 'left'

            # fill the sky
            self.screen.fill(sky)

            # Looping
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        player.shoot()
                        c = Cement(player.rect.x, player.rect.y + 35)
                        cements.append(c)
                        allObjGroup.add(c)
                        collGroup.add(c)
                    else:
                        player.move(event.key, playerHB)

            # move every cement
            for c in range(len(cements)):
                cements[c].rect.x += 10

            # remove cements that left the game window
            for cement in cements:
                if cement.rect.x > 810:
                    cements.remove(cement)
                    allObjGroup.remove(cement)
                    collGroup.remove(cement)

            # handling obstacles
            if Objects.createObject(0.01):
                # which object will be created
                obj = choice(objects)
                if obj == 'H':
                    h = Hydrant()
                    hydrants.append(h)
                    allObjGroup.add(h)
                    collGroup.add(h)
                elif obj == 'B':
                    m = Manhole()
                    manholes.append(m)
                    allObjGroup.add(m)
                    collGroup.add(m)

            # object handling
            for h in range(len(hydrants)):
                hydrants[h].rect.x -= 10

            for hydrant in hydrants:
                if hydrant.rect.x < -30:
                    hydrants.remove(hydrant)
                    allObjGroup.remove(hydrant)
                    collGroup.remove(hydrant)

            for m in range(len(manholes)):
                manholes[m].rect.x -= 10

            for manhole in manholes:
                if manhole.rect.x < -50:
                    manholes.remove(manhole)
                    allObjGroup.remove(manhole)
                    collGroup.remove(manhole)

            # handle animations
            player.animate(cements)

            # player
            allObjGroup.add(player)
            allObjGroup.add(playerHB)

            # draw
            backScenarioGroup.draw(self.screen)
            frontScenarioGroup.draw(self.screen)
            allObjGroup.draw(self.screen)

            # check collision
            if pygame.sprite.spritecollide(playerHB, collGroup, False):
                done = True

            pygame.display.update()
            self.fpsClock.tick(self.fps)

        #pygame.time.wait(5000)
        pygame.quit()


if __name__ == "__main__":
    MainWindow = LCM_Main()
    MainWindow.MainLoop()
