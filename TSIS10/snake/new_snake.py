from random import randint, randrange
import psycopg2
import csv
import pygame

username = input()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Diora040917"
)

current = conn.cursor()

sql = """
    SELECT * FROM snake WHERE user_name = %s;
"""
current.execute(sql, [username])
data = current.fetchone()


try:
    score = data[1]
    highscore = data[2]
    level = data[3]
except:
    score = 0
    highscore = 0
    level = 0

if data == None:
    sql = """
        INSERT INTO snake VALUES(%s, 0, 0, 0);
    """
    current.execute(sql, [username])
    conn.commit()
pygame.init()

WIDTH, HEIGHT = 600, 580
FPS = 5
cell = 40

font = pygame.font.SysFont("Proxima Nova", 40, True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)

image = pygame.image.load('tsis8/bcground.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

finished = False

clock = pygame.time.Clock()
# CLASS FOOD
class Food:
    def __init__(self):
        # self.x = randint(0, WIDTH) % cell * 40
        # self.y = randint(0, HEIGHT) % cell * 40
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
        if level == 1:
            self.x = randrange(cell, WIDTH - cell, cell)
            self.y = randrange(0, HEIGHT, cell)
        if level > 1:
            self.x = randrange(cell, WIDTH - cell, cell)
            self.y = randrange(cell, HEIGHT - cell, cell)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))

    def redraw(self):
        self.x = randrange(cell, WIDTH - cell, cell)
        self.y = randrange(cell, HEIGHT - cell, cell)
# CLASS SNAKE
class Snake:
    def __init__(self):
        self.speed = cell
        self.score = 0
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color,
                             (block[0], block[1], cell, cell))

    def collide_food(self, f: Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            f.redraw()
            self.score += 1
            self.body.append([1000, 1000])

    def collide_self(self):
        global finished
        if self.body[0] in self.body[1:]:
            finished = True

    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()

s = Snake()
f = Food()

while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True

    
    screen.blit(pygame.transform.scale(image, (600,580)), (0, 0))

    if s.score in range(10, 15):
        level = 2
        FPS = 7
    if s.score in range(15, 20):
        level = 3
        FPS = 9
    if s.score in range(20,25):
        level = 4
        FPS = 11
    if score in range(25, 30):
        level = 5
        FPS = 13
    if score >= 30:
        level = 6
        FPS = 17

    if score > highscore:
        highscore = score
        sql = """
        UPDATE snake SET score = %s, highscore = %s, level = %s WHERE user_name = %s;
        """
        current.execute(sql, [score, highscore, level, username])

    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

    text = font.render(f"Score:{s.score}", True, WHITE)
    text2 = font.render(f"Level: {level}", True, WHITE)
    text3 = font.render(f"Highscore: {highscore}", True, WHITE)
    screen.blit(text, (0, 0))
    screen.blit(text2, (0, 40))
    screen.blit(text3,(0,80))
    pygame.display.flip()
    score = s.score
pygame.quit()
if score > highscore:
    highscore = score
    score = score
    level = level
    sql = """
        UPDATE snake SET score = %s, highscore = %s, level = %s WHERE user_name = %s;
    """
    current.execute(sql, [score, highscore, level, username])
else:
    score = score
    level = level
    sql = """
        UPDATE snake SET score = %s, level = %s WHERE user_name = %s;
    """
    current.execute(sql,[score, level, username])
sql = """
    SELECT * FROM snake;
"""
current.execute(sql, [username])
data = current.fetchall()
print(*data, sep = ",")

f = open("SCORE TABLE.csv", 'w')
writer = csv.writer(f)

writer.writerow(data)
f.close()

conn.commit()
current.close()
conn.close() 