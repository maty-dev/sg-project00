# -*- coding: utf-8 *-*
import pygame, sys
from pygame.locals import *
import components

pygame.init()

def main():
    screen=pygame.display.set_mode((500,500))
    fps=pygame.time.Clock()
    pointer=components.Pointer()
    gameOn=True

    while(gameOn):
        events=pygame.event.get()
        for event in events:
            if(event.type==pygame.QUIT):
                gameOn=False
            elif(even.type==pygame.KEYDOWN):
                if (event.key==pygame.K_ESCAPE):
                    gameOn==False
        screen.fill((000,000,000))
        pygame.display.flip()

main()
pygame.quit()
sys.exit()
