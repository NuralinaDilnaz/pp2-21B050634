#creating
import pygame 

#initialization
pygame.init() 
WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DRAWING AN EQUILATERAL TRIANGLE")

#RGB system
WHITE = (255, 255, 255) 

#drawing an equilateral triangle
pygame.draw.polygon(SCREEN, WHITE, ((100, 100), (0,200),(200, 200)), 3) 

pygame.display.flip() 
while True:
  pass
