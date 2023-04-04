#creating
import pygame as pg  # short version of python to save time, rather writing python 
import random


WIDTH, HEIGHT = 640, 500
FPS = 60

#RGB system of colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
score = 0
y = 0
ry = 2

MEGA_COIN = pg.USEREVENT + 1
FLIP = pg.USEREVENT + 2

#initialization
pg.init()

#display setting
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("RACER")

font = pg.font.SysFont('Times New Roman', 40)
pg.time.set_timer(FLIP, 150)

road = pg.image.load('tsis8/road.png')

#sprites
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('tsis8/car.png')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(center=(400, 500))
        self.speed = 3

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('tsis8/enemy.png')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(3, 5)

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20, 20))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(1, 8)
        self.animation_index = 0
        self.random_number = random.randint(0, 9)
        self.images = [
            r'tsis8/c1.png',
            r'tsis8/c2.png',
            r'tsis8/c3.png',
            r'tsis8/c4.png',
            r'tsis8/c5.png'
        ]
        self.image = pg.image.load(self.images[0])
        self.mega_coin()

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (20, 20)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = pg.image.load(self.images[self.animation_index])

    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def mega_coin(self):
        if self.random_number in [0, 1, 2]:
            self.image = pg.image.load(self.images[1])
            # self.speed = 15
        else:
            self.image = pg.image.load(self.images[0])

    def is_mega_coin(self):
        return self.random_number == 5


P1 = Player()
enemies = pg.sprite.Group([Enemy() for _ in range(3)])
coins = pg.sprite.Group([Coin() for _ in range(5)])

#GAME LOOP
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == MEGA_COIN:
            P1.speed = 30
        if event.type == FLIP:
            for coin in coins:
                coin.animate()

    screen.fill(WHITE)
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, y % HEIGHT))
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, -HEIGHT + (y % HEIGHT)))

    y += ry

    P1.draw()
    P1.move()
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.kil()

    for coin in coins:
        coin.draw()
        coin.move()
        coin.animate()
        coin.kil()

    if enemies.__len__() < 3:
        enemies.add(Enemy())

    if coins.__len__() < 5:
        coins.add(Coin())

    if pg.sprite.spritecollide(P1, enemies, False):
        running = False

    for coin in pg.sprite.spritecollide(P1, coins, True):
        score += 1
        if coin.is_mega_coin():
            score += 100
            pg.time.set_timer(MEGA_COIN, 5000, loops=False)


    text = font.render(f"{score}", True, BLACK)
    screen.blit(text, (20, 20))

    pg.display.update()
pg.quit()