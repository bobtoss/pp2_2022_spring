import pygame
import datetime
width,height = 800, 800
pygame.init()
screen=pygame.display.set_mode([width,height])
pygame.display.set_caption('MICKEY CLOCK')
clock=pygame.time.Clock()
fps=60

image= pygame.image.load('mickeyclock.jpeg').convert()
hand1=pygame.image.load('mikey_hand1.png').convert_alpha()
hand2=pygame.image.load('mikey_hand2.png').convert_alpha()

while True:
    screen.fill(pygame.Color('white'))

    screen.blit(image,(-240,-80))

    key = pygame.key.get_pressed()

    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    
    anglesecond=second*6-56
    angleminute=minute*6+50

    img=pygame.transform.rotate(hand1,-anglesecond)
    x=img.get_width()/2
    y=img.get_height()/2
    img2=pygame.transform.rotate(hand2,-angleminute)
    x2=img2.get_width()/2
    y2=img2.get_height()/2


    screen.blit(img,(400-int(x), 400-int(y)))
    screen.blit(img2,(400-int(x2), 400-int(y2)))

    for event in pygame.event.get():
        if key[pygame.K_SPACE]:
            exit()

    pygame.display.flip()
    clock.tick(fps)