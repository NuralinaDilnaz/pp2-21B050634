import pygame
from datetime import datetime

pygame.init()

def rotateCenter(s,image,tl,angle):
        ro_image=pygame.transform.rotate(image,angle)
        new_rect=ro_image.get_rect(center=image.get_rect(topleft=tl).center)

        s.blit(ro_image,new_rect)

size=(800,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('clock.py')

image=pygame.image.load('C:/Users/Lenovo/Desktop/pp2-21B050634/tsis7/mickey.jpeg')
image=pygame.transform.scale(image,size)
r1=pygame.image.load('tsis7/r1.png')
r2=pygame.image.load('tsis7/r2.png')

clock=pygame.time.Clock()
done=False

def time(time):
        return 3600-time*6

while not done:
        clock.tick(60)

        for event in pygame.event.get():
         if event.type==pygame.QUIT:
                 done=True

        screen.blit(image,(0,0))

        n=datetime.now()

        angle_s=time(n.second+1)
        angle_m=time(n.minute)

        rotateCenter(screen,r1,(180,90),angle_s)
        rotateCenter(screen,r2,(180,90),angle_m)
        pygame.display.flip()
pygame.quit()