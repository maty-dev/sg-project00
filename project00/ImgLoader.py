# -*- coding: utf-8 *-*
import pygame, sys
from pygame.locals import *

pygame.init()

def AddTransparency(images):
    try:
        pos=0
        for i in images:
            color=i.get_at((0,0))
            images[pos].set_colorkey(color)
            pos+=1
        return images
    except TypeError:
        color=images.get_at((0,0))
        images.set_colorkey(color)
        return images

def LoadPlayerImgs():
    playerSuffix="images/Player/"
    playerUp=[]
    playerDown=[]
    playerLeft=[]
    playerRight=[]
    playerUp.append(pygame.image.load(playerSuffix+"Up.PNG"))
    playerUp.append(pygame.image.load(playerSuffix+"Up1.PNG"))
    playerUp.append(pygame.image.load(playerSuffix+"Up2.PNG"))
    #playerUp.append(pygame.image.load(playerSuffix+"Up3.PNG"))
    #playerUp.append(pygame.image.load(playerSuffix+"Up4.PNG"))
    #playerUp.append(pygame.image.load(playerSuffix+"Up5.PNG"))
    #playerUp.append(pygame.image.load(playerSuffix+"Up6.PNG"))
    playerDown.append(pygame.image.load(playerSuffix+"Down.PNG"))
    playerDown.append(pygame.image.load(playerSuffix+"Down1.PNG"))
    playerDown.append(pygame.image.load(playerSuffix+"Down2.PNG"))
    #playerDown.append(pygame.image.load(playerSuffix+"Down3.PNG"))
    #playerDown.append(pygame.image.load(playerSuffix+"Down4.PNG"))
    #playerDown.append(pygame.image.load(playerSuffix+"Down5.PNG"))
    #playerDown.append(pygame.image.load(playerSuffix+"Down6.PNG"))
    playerRight.append(pygame.image.load(playerSuffix+"Right.PNG"))
    playerRight.append(pygame.image.load(playerSuffix+"Right1.PNG"))
    playerRight.append(pygame.image.load(playerSuffix+"Right2.PNG"))
    #playerRight.append(pygame.image.load(playerSuffix+"Right3.PNG"))
    #playerRight.append(pygame.image.load(playerSuffix+"Right4.PNG"))
    #playerRight.append(pygame.image.load(playerSuffix+"Right5.PNG"))
    #playerRight.append(pygame.image.load(playerSuffix+"Right6.PNG"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left.PNG"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left1.PNG"))
    playerLeft.append(pygame.image.load(playerSuffix+"Left2.PNG"))
    #playerLeft.append(pygame.image.load(playerSuffix+"Left3.PNG"))
    #playerLeft.append(pygame.image.load(playerSuffix+"Left4.PNG"))
    #playerLeft.append(pygame.image.load(playerSuffix+"Left5.PNG"))
    #playerLeft.append(pygame.image.load(playerSuffix+"Left6.PNG"))
    playerAtkLeft=pygame.image.load(playerSuffix+"AtkLeft.PNG")
    playerAtkRight=pygame.image.load(playerSuffix+"AtkRight.PNG")
    playerAtkDown=pygame.image.load(playerSuffix+"AtkDown.PNG")
    playerAtkUp=pygame.image.load(playerSuffix+"AtkUp.PNG")
    playerUP=AddTransparency(playerUp)
    playerDown=AddTransparency(playerDown)
    playerRight=AddTransparency(playerRight)
    playerLeft=AddTransparency(playerLeft)
    playerAtkLeft=AddTransparency(playerAtkLeft)
    playerAtkRight=AddTransparency(playerAtkRight)
    playerAtkDown=AddTransparency(playerAtkDown)
    playerAtkUp=AddTransparency(playerAtkUp)
    playerImgs={"UP":playerUp,"DOWN":playerDown,"RIGHT":playerRight,"LEFT":playerLeft,"ATK_LEFT":playerAtkLeft,"ATK_RIGHT":playerAtkRight,"ATK_UP":playerAtkUp,"ATK_DOWN":playerAtkDown}
    return playerImgs

def LoadBackgroundImage(zoneParam="testArea"):
    backgroundSuffix="zones/"+zoneParam+"/Background/"
    background=pygame.image.load(backgroundSuffix+"Background.png")
    return background

def LoadTile(zoneParam):
    pass
