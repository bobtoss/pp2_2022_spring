import random
import sys
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE  = 0
coin_SCORE = 0 #
coin_bool=False #
diamond_bool=False#

clock = pygame.time.Clock()


score_font = pygame.font.SysFont("Verdana", 20)
coin_score_font=pygame.font.SysFont("Verdana",20) #

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load("AnimatedStreet.png")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#my code
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        

    def update(self):
        global coin_SCORE
        global coin_bool
        global ENEMTY_STEP
        self.rect.move_ip(0, STEP)

        if coin_bool==True:
            coin_SCORE+=1
            if coin_SCORE % 5==0:
                ENEMTY_STEP+=1
            coin_bool=False
            self.rect.center = (random.randint(30, 350), 0)

        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#my code
class Diamonds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("diamond.jpg")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        

    def update(self):
        global coin_SCORE
        global diamond_bool
        global ENEMTY_STEP
        self.rect.move_ip(0, STEP)

        if diamond_bool==True:
            coin_SCORE+=2
            if coin_SCORE%5==0:
                ENEMTY_STEP+=1
            diamond_bool=False
            self.rect.center = (random.randint(30, 350), 0)

        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coins() #
D1 = Diamonds() #

enemies = pygame.sprite.Group()
enemies.add(E1)

coin =pygame.sprite.Group() #
coin.add(C1) #

diamond = pygame.sprite.Group() #
diamond.add(D1) #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, coin): #
        coin_bool=True
    if pygame.sprite.spritecollideany(P1,diamond):
        diamond_bool=True
        
    SURF.blit(bg, (0, 0))
    P1.update()
    E1.update()
    C1.update() #
    D1.update() #
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF) #
    D1.draw(SURF) #
    

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))
    coin_score_img = coin_score_font.render("coins: " +str(coin_SCORE), True, (255,0,0)) #
    SURF.blit(coin_score_img, (290, 10)) #
    

    pygame.display.update()
    clock.tick(FPS)