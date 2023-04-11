#creating
import pygame
from pygame.locals import *

#initializing
pygame.init()
WIDTH = 600
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DRAWING A RHOMBUS")

clock = pygame.time.Clock()
FPS = 30

# RHOMBUS points 
diamondWidth = 80
diamondHeight = 100

pos1 = (WIDTH/2, HEIGHT/2 - diamondHeight/2)
pos2 = (pos1[0] - diamondWidth/2, pos1[1] + diamondHeight/2)
pos3 = (pos1[0], pos1[1]+diamondHeight)
pos4 = (pos2[0]+diamondWidth, pos2[1])

points_0 = [pos1, pos2, pos3, pos4]

points = [(p[0]+diamondWidth+10, p[1]) for p in points_0]

running = False
while not running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = True

    SCREEN.fill((0, 0, 0))

    # Drawing empty diamond with thickness 4
    pygame.draw.polygon(SCREEN, (0, 255, 255), points , 4)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()