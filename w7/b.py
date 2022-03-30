import pygame
pygame.init()
playlist = list()
playlist.append ( "Кайрат Нуртас - Алматынын тундери-ай.mp3" )
playlist.append ( "Кайрат Нуртас - My Universe.mp3" )
playlist.append('Мухтар Ханзада - Шаршамай.mp3')

width,height = 400, 400
screen=pygame.display.set_mode([width,height])
pygame.display.set_caption(playlist[0])
pygame.mixer.music.load ( playlist[0])  

pygame.mixer.music.play(1)

move_ticker = 0

pause=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key==pygame.K_LEFT:
                if move_ticker==0:
                    move_ticker=len(playlist)-1
                elif move_ticker>0:
                    move_ticker-=1
                pygame.mixer.music.load(playlist[move_ticker])
                pygame.display.set_caption(playlist[move_ticker])
                pygame.mixer.music.play(1)
            elif event.key==pygame.K_RIGHT:
                if move_ticker==len(playlist)-1:
                    move_ticker=0
                elif move_ticker<len(playlist)-1:
                    move_ticker+=1
                pygame.mixer.music.load(playlist[move_ticker])
                pygame.display.set_caption(playlist[move_ticker])
                pygame.mixer.music.play(1)

            
