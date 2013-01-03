# -*- coding: utf-8 *-*
import pygame, sys
from pygame.locals import *

pygame.init()

def AddTransparency(images):
    pos=0
    for i in images:
        color=i.get_at((0,0))
        images[pos].set_colorkey(color)
        pos+=1
    return images

def LoadPlayerImgs():
    playerSuffix="images/Player/"
    playerUp=[]
    playerDown=[]
    playerLeft=[]
    playerRight=[]
    playerUp.append(pygame.image.load(playerSuffix+"Up.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up1.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up2.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up3.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up4.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up5.png"))
    playerUp.append(pygame.image.load(playerSuffix+"Up6.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down1.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down2.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down3.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down4.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down5.png"))
    playerDown.append(pygame.image.load(playerSuffix+"Down6.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right1.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right2.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right3.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right4.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right5.png"))
    playerRight.append(pygame.image.load(playerSuffix+"Right6.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left1.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left2.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left3.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left4.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left5.png"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left6.png"))
    playerUP=AddTransparency(playerUp)
    playerDown=AddTransparency(playerDown)
    playerRight=AddTransparency(playerRight)
    playerLeft=AddTransparency(playerLeft)
    playerImgs={"UP":playerUp,"DOWN":playerDown,"RIGHT":playerRight,"LEFT":playerLeft}
    return playerImgs

def LoadBackground():
    backgroundSuffix="images/Background/"
    background=pygame.image.load(backgroundSuffix+"backgroundArt2.png")
    return background
