# -*- coding: utf-8 *-*
import pygame, sys
from pygame.locals import *

pygame.init()

def AddTransparency(images):
    pos=0
    for i in images:
        color=i.get_at((0,0))
        images[pos].set_colorkey(color,RLEACCEL)
        pos+=1

def LoadPlayerImgs():
    playerSuffix="images/Player/"
    playerUp=[]
    playerDown=[]
    playerLeft=[]
    playerRight=[]
    playerUp.append(pygame.image.load(playerSuffix+"Up.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up1.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up2.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down1.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down2.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right1.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right2.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left1.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left2.png"))
    AddTransparency(playerUp)
    AddTransparency(playerDown)
    AddTransparency(playerRight)
    AddTransparency(playerLeft)
    playerImgs={"UP":playerUp,"DOWN":playerDown,"RIGHT":playerRight,"LEFT":playerLeft}
    return playerImgs

def LoadBackground():
    backgroundSuffix="images/Background/"
    background=pygame.image.load(backgroundSuffix+"backgroundArt2.png")
    return background
