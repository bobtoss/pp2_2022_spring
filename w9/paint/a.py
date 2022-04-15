from turtle import position, width
import pygame
from pygame.constants import KEYDOWN
# colors
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)
white = (255,255,255)
color = white #default color

#
def drawRhombus():
    
    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        

    isMouseDown = False

    while True:
        global color,green,yellow,red,blue,white
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0
        x1 = prevX
        x2 = currentX
        y1 = prevY
        y2 = currentY
        width=7
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)
        
        pygame.display.flip()
        clock.tick(60)
    
#
def drawSquare():
    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        global color,yellow,blue,green,red
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0
        
        x1 = prevX
        x2 = currentX
        y1 = prevY
        y2 = currentY
        mn = min(abs(x2 - x1), abs(y2 - y1))
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            screen.blit(baseLayer, (0, 0))        
            if x2 > x1 and y2 > y1:
                pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
            if y2 > y1 and x1 > x2:
                pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
            if x1 > x2 and y1 > y2:
                pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
            if x2 > x1 and y1 > y2:
                pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))
            
            #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
        
        pygame.display.flip()
        clock.tick(60)
        
#
def drawEquilateralTriangle():
    
    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        global color,yellow,blue,green,red
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0
        x1 = prevX
        x2 = currentX
        y1 = prevY
        y2 = currentY

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))        
             if x2 > x1 and y2 > y1:
                pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
             if y2 > y1 and x1 > x2:
                pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
             if x1 > x2 and y1 > y2:
                pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
             if x2 > x1 and y1 > y2:
                pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
             
             #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
        
        pygame.display.flip()
        clock.tick(60)

#
def drawTriangle():
    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        global color,green,yellow,red,blue,white
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0
        x1 = currentX
        x2 = prevX
        y1 = currentY
        y2 = prevY
        width_b = abs(x2 - x1)
        height = (3**0.5) * width_b / 2
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             
             if y2 > y1:
                x1 = prevX
                x2 = currentX
                y1 = prevY
                y2 = currentY
                width_b = abs(x2 - x1)
                height = (3**0.5) * width_b / 2
                pygame.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height))   )
             else:
                x1 = currentX
                x2 = prevX
                y1 = currentY
                y2 = prevY
                width_b = abs(x2 - x1)
                height = (3**0.5) * width_b / 2
                pygame.draw.polygon(screen, color , ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))
             #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
        
        pygame.display.flip()
        clock.tick(60)
        
#
def circle():
    

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        global color,green,yellow,red,blue,white
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             c = calculateCenter(prevX, prevY, currentX, currentY)
             r = calculateRadius(prevX, prevY, currentX, currentY)
             pygame.draw.circle(screen, color ,c, r)
             #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
        
        pygame.display.flip()
        clock.tick(60)

#
def rect():
    

    #baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        global color,yellow,blue,green,red
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                if event.key == pygame.K_y:
                    color = yellow
                if event.key == pygame.K_b:
                    color = blue
                if event.key == pygame.K_g:
                    color = green
                if event.key == pygame.K_w:
                    color = white
                if event.key == pygame.K_x:
                    return 0
        

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             r = calculateRect(prevX, prevY, currentX, currentY)
             pygame.draw.rect(screen, color ,pygame.Rect(r), 1)
             #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
        
        pygame.display.flip()
        clock.tick(60)

# function to calculate rectangular       
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#
def eraser():
    
    clock = pygame.time.Clock()
    
    prevX = 0
    prevY = 0
    
    #screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        currentX = prevX
        currentY = prevY
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False
                    baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                currentX =  event.pos[0]
                currentY =  event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return 0
                
        
        if isMouseDown:
            pygame.draw.line(screen, (0, 0,0), (prevX, prevY), (currentX, currentY),10)

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)

#functions to calculate cicrle center and radius      
def calculateCenter(x1, y1, x2, y2):
    return [min(x1,x2)+abs(x1-x2)/2,min(y1,y2)+abs(y1-y2)/2]
def calculateRadius(x1, y1, x2, y2):
    return int(abs(x1-x2)/2)

#body of our code
pygame.init()
screen = pygame.display.set_mode((640, 480))
baseLayer = pygame.Surface((640, 480))
screen.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_r:
                rect()
            if event.key == pygame.K_c:
                circle()
            if event.key == pygame.K_e:
                eraser()
            if event.key == pygame.K_h:
                drawRhombus()
            if event.key == pygame.K_t:
                drawTriangle()
            if event.key == pygame.K_d:
                drawEquilateralTriangle()
            if event.key == pygame.K_s:
                drawSquare()