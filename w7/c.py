import pygame
#from pygame.constants import K_DOWN
pygame.init()
screen = pygame.display.set_mode((800, 800))
center1=400
center2=400
clock=pygame.time.Clock()

while True:
    screen.fill((0, 0, 255))    
    pygame.draw.circle(screen, (255, 0, 0),[center1, center2], 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if center1<=20:
                    center1=0
                else:
                    center1-=20
            elif event.key==pygame.K_RIGHT:
                if center1>=780:
                    center1=800
                else:
                    center1+=20
            elif event.key==pygame.K_DOWN:
                if center2>=780:
                    center2=800
                else:
                    center2+=20
            elif event.key==pygame.K_UP:
                if center2<=20:
                    center2=0
                else:
                    center2-=20

    pygame.display.update() 
    pygame.display.flip()

    clock.tick(120)
 