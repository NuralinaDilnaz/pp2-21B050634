import pygame as pg
from random import randint, randrange
import time

pg.init()

lose = False
FPS = 5
cell = 40 
image = pg.image.load('tsis8/bcground.png')
score = 0
font_score = pg.font.SysFont('Verdana', 30, True, True)
rand_food = 0
levelcnt = pg.font.SysFont('Verdana', 30, True, True)
current_lev = 1
WIDTH = 640
HEIGHT = 500
FPS = 5

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)
WALLCOLOR = (127, 72, 41)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('SNAKE')
lose_im = pg.image.load('tsis8/you_lose.png')
running = True

clock = pg.time.Clock()

class Food:
    def __init__(self): 
        global rand_food
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
        self.rand = randint(0, 2)
        rand_food = self.rand
        self.im = pg.image.load('tsis8/c1.png')
        
    def draw(self):

        screen.blit(self.im, (self.x, self.y)) # picture of food
        
    def redraw(self): #position for food, so that it does not fall on a snake
        global rand_food
        self.rand = randint(0, 2)
        self.im = pg.image.load('tsis8/c2.png')
        rand_food = self.rand
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80]]
        self.dx = self.speed
        self.dy = 0
        self.direction = ''
        self.color = (10, 30, 100)
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.direction = 'left'
                if event.key == pg.K_RIGHT and self.direction != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.direction = 'right'
                if event.key == pg.K_UP and self.direction != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.direction = 'up'
                if event.key == pg.K_DOWN and self.direction != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.direction = 'down'

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WIDTH  #collisions
        self.body[0][1] %= HEIGHT

    def draw(self): 
        pg.draw.rect(screen, self.color, (self.body[0][0], self.body[0][1], cell, cell)) # painting head of my snike in different colour

        for block in self.body[1:]: # painting body
            pg.draw.rect(screen, TEAL, (block[0], block[1], cell, cell))
    
    def collision_food(self, f:Food): 
        if self.body[0][0] == f.x and self.body[0][1] == f.y: # collision with the food
            global score
            if rand_food == 0:
                score += 10
            elif rand_food == 1:        # increment of cnt
                score += 20
            elif rand_food == 2:
                score += 30
           
            self.body.append([1000, 1000])
    
    def collision_self(self):
        global running, lose
        if self.body[0] in self.body[1:]: # collision with himself
            lose = True

    def eat_food(self, f:Food):
        if [f.x, f.y] in self.body: # repainting the snake in collision with the food
            f.redraw()

S1 = Snake()
F1 = Food()
pg.time.set_timer(pg.USEREVENT, 5000) # timer for food's vanishing away

level = 0

while running:
    clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.USEREVENT:
            F1.redraw() 
        
    screen.blit(pg.transform.scale(image, (800,800)), (0, 0))
    
    if score >= 100 and score < 350:  # transitions for the next levels    
        level = 1                      
        FPS = 7
        current_lev = 2

    if score >= 350:
        level = 2
        current_lev = 3
        FPS = 10    

    F1.draw()
    S1.draw()
    S1.move(events)
    S1.collision_food(F1)
    S1.collision_self()
    S1.eat_food(F1)

    textscore = font_score.render(f'Score: {score}', True, WHITE)
    textlvl = levelcnt.render(f'Level: {current_lev}', True, WHITE)
    #current score
    screen.blit(textscore, (20, 10)) 
    #current level
    screen.blit(textlvl, (650, 10)) 

    #window for the losee
    while lose: 
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        screen.blit(pg.transform.scale(lose_im, (800, 800)), (0, 0))
        
        pg.display.flip()
    pg.display.flip()

pg.quit()
