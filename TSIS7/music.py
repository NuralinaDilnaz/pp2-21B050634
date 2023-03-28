import pygame

pygame.init()

size=(900,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('my_playlist')
image=pygame.image.load('tsis7/cute.jpg')

music=list()
music.append('tsis7/Connected.mp3')
pygame.mixer.music.load(music.pop())
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()


done=False

def right():
    global music
    music=music[1:]+[music[0]]
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play()


def left():
    global music
    music=[music[-1]]+music[:-1]
    pygame.mixer.music.load(music[0])
    pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pygame.mixer.music.stop()
                left()
            if event.key==pygame.K_RIGHT:
                pygame.mixer.music.stop()
                right()
            if event.key==pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key==pygame.K_CAPSLOCK:
                pygame.mixer.music.unpause()
    
    #screen.fill((255,255,255))
    screen.blit(image,(0,0))

    pygame.display.flip()
pygame.quit()
