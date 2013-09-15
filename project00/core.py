# -*- coding: utf-8 *-*
import pygame, sys
from pygame.locals import *
import components
import ImgLoader
import GameModel


pygame.init()

def AnimTime(t):
    t+=1
    if(t>1):
        t=0
    return t

def main():
    screen=pygame.display.set_mode((500,500))
    defFont=pygame.font.Font(None,25)
    fps=pygame.time.Clock()
    pointer=components.Pointer()
    playerImgs=ImgLoader.LoadPlayerImgs()
<<<<<<< HEAD
    background=ImgLoader.LoadBackground()
    player=GameModel.Player(playerImgs,"Dummi3")
    background=components.Background(ImgLoader.LoadBackground(),True)
=======
    player=GameModel.Player(playerImgs,"Dummi3")
    background=components.Background(ImgLoader.LoadBackgroundImage(),True)
>>>>>>> 8eb61447ba854a487814af399bef19508daf1e0d
    gameOn=True
    time=0

    while(gameOn):
        events=pygame.event.get()
        for event in events:
            if(event.type==pygame.QUIT):
                gameOn=False
            elif(event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_ESCAPE):
                    gameOn==False
        fps.tick(25)
        time=AnimTime(time)
        screen.fill((000,000,000))
        player.Update(events,time)
        background.Update(player.x,player.y)
        background.Render(screen)
        player.Render(screen)
<<<<<<< HEAD
        screen.blit(defFont.render(player.name,0,(255,255,255)),((player.x+230),(player.y+170)))
=======
        screen.blit(defFont.render(player.name,0,(255,255,255)),((player.x+200),(player.y+170)))
>>>>>>> 8eb61447ba854a487814af399bef19508daf1e0d
        pygame.display.flip()


main()
pygame.quit()
sys.exit()
