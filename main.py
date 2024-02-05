import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

aylxo = pygame.image.load('Piet Flex.JPG')
goku = pygame.image.load('goku.jpg')

xVal = 0
while True:
    #EVENT CHECKER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #CHANGING VAL
    xVal += 2
    
    #LOGIC
    if xVal > width:
        xVal = 0
      
    #DRAWING
    screen.blit(goku, (0,0))
    screen.blit(aylxo, (xVal, 200))
    pygame.display.update()
    
    clock.tick(60)