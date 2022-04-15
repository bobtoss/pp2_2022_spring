from os import scandir
from select import select
import sys
import pygame
import random

from pygame.time import Clock
pygame.init()

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400

BLOCK_SIZE = 20
step=5#
img = pygame.image.load("snake_font.png") #
img1 = pygame.transform.scale(img,(400,400)) #
score_font = pygame.font.SysFont("Times New Roman", 20) #
level_font=pygame.font.SysFont("Times New Roman", 20)#
score=0#
Level=1#


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        f = open("levels/level1.txt".format(level), "r")

        #lines = content.split('\n')
        #print(len(lines[0]))
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (128,128,128), rect)
    def check_collision(self, snake,): #
        for point in self.body:
                if snake.body[0].x == point.x:
                    if snake.body[0].y == point.y:
                        pygame.quit()
    
            

class Food:
    def __init__(self):
        self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20))) #

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (128, 0, 0), rect)
    def check_collision(self, snake): #
        if snake.body[0].x == self.location.x:
            if snake.body[0].y == self.location.y:
                self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                point = self.location
                rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, (128, 0, 0), rect) 
    def check_new(self,wall): #
        for point in wall.body:
            if point.x == self.location.x:
                if point.y == self.location.y:
                    self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                    point = self.location
                    rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, (128, 0, 0), rect) 



class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
        #
        if self.body[0].x * BLOCK_SIZE > WIDTH:
           # self.body[0].x = 0
           pygame.quit()
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
           # self.body[0].y = 0
           pygame.quit()

        if self.body[0].x < 0:
           # self.body[0].x = WIDTH / BLOCK_SIZE
           pygame.quit()
        
        if self.body[0].y < 0:
           # self.body[0].y = HEIGHT / BLOCK_SIZE
           pygame.quit()#
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, 20, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 128, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 128, 0), rect)

    def check_collision(self, food): #
        global score,step,Level
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                score+=1
                if score%5==0 and score >4:
                    step+=3
                    Level+=1
    
    
    
    

def main():
    global SCREEN, CLOCK,step,score
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()
    wall = Wall(snake.level)
    game=True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
        snake.move()
        SCREEN.blit(img1,(0,0))

        snake.check_collision(food)
        food.check_collision(snake)
        food.check_new(wall)
        wall.check_collision(snake)
        #snake.speed()

        
            

        #SCREEN.fill(BLACK)

        
        snake.draw()
        food.draw() #
        wall.draw()
        
        #drawGrid()
        #
        score_img = score_font.render(f'SCORE: {str(score)}', True, pygame.Color('white'))
        SCREEN.blit(score_img, (0, 0))
        score_img1 = score_font.render(f'LEVEL: {str(Level)}', True, pygame.Color('white'))
        SCREEN.blit(score_img1, (0, 20))
        #

        pygame.display.update()
        CLOCK.tick(step)#





main()