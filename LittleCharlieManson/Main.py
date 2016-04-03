import pygame, sys
from pygame.locals import*

pygame.init()

fps = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Little Charlie Manson')

sky = (0, 152, 248)

#Animation Direction
direction = 'left'

#Sprites
grassImg = pygame.image.load('gramado.png')
sunImg = pygame.image.load('sol1.png')
cloudImg = pygame.image.load('nuvens.png')
streetImg = pygame.image.load('rua.png')
streetLines = pygame.image.load('faixasrua.png')
grassDetails = pygame.image.load('grama1.png')
streetDetails = pygame.image.load('faixascalcada.png')
player = pygame.image.load('Charlinho.png')

#Sprites Position
grassX = 1
grassY = 1
cloudX = 1
cloudY = 1
ImgX = 1
ImgY = 1
playerX = 10
PlayerY = 470

while True:
    #Scene Animation
    if direction == 'left':
        cloudX-=5
        grassX-=5
        if cloudX < -800 and cloudX > -900:
            direction = 'right'
    elif direction == 'right':
        cloudX = 800
        grassX = 0
        if cloudX == 800:
            direction = 'left'
    
    #Loading Sprites in scene        
    screen.fill(sky)
    screen.blit(grassImg,(ImgX,ImgY))
    screen.blit(cloudImg,(cloudX,cloudY))
    screen.blit(streetImg,(ImgX,ImgY))
    screen.blit(sunImg,(ImgX,ImgY))
    screen.blit(streetLines,(ImgX,ImgY))
    screen.blit(grassDetails,(grassX,grassY))
    screen.blit(streetDetails,(ImgX,ImgY))
    screen.blit(player,(playerX,PlayerY))
    
    #Looping
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)