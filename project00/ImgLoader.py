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

def LoadImgs(suf, atkImgs=True):
    Suffix=suf
    atk=atkImgs
    Up=[]
    Down=[]
    Left=[]
    Right=[]
    Up.append(pygame.image.load(Suffix+"Up.PNG"))
    Up.append(pygame.image.load(Suffix+"Up1.PNG"))
    Up.append(pygame.image.load(Suffix+"Up2.PNG"))
    #Up.append(pygame.image.load(Suffix+"Up3.PNG"))
    #Up.append(pygame.image.load(Suffix+"Up4.PNG"))
    #Up.append(pygame.image.load(Suffix+"Up5.PNG"))
    #Up.append(pygame.image.load(Suffix+"Up6.PNG"))
    Down.append(pygame.image.load(Suffix+"Down.PNG"))
    Down.append(pygame.image.load(Suffix+"Down1.PNG"))
    Down.append(pygame.image.load(Suffix+"Down2.PNG"))
    #Down.append(pygame.image.load(Suffix+"Down3.PNG"))
    #Down.append(pygame.image.load(Suffix+"Down4.PNG"))
    #Down.append(pygame.image.load(Suffix+"Down5.PNG"))
    #Down.append(pygame.image.load(Suffix+"Down6.PNG"))
    Right.append(pygame.image.load(Suffix+"Right.PNG"))
    Right.append(pygame.image.load(Suffix+"Right1.PNG"))
    Right.append(pygame.image.load(Suffix+"Right2.PNG"))
    #Right.append(pygame.image.load(Suffix+"Right3.PNG"))
    #Right.append(pygame.image.load(Suffix+"Right4.PNG"))
    #Right.append(pygame.image.load(Suffix+"Right5.PNG"))
    #Right.append(pygame.image.load(Suffix+"Right6.PNG"))
    Left.append(pygame.image.load(Suffix+"Left.PNG"))
    Left.append(pygame.image.load(Suffix+"Left1.PNG"))
    Left.append(pygame.image.load(Suffix+"Left2.PNG"))
    #Left.append(pygame.image.load(Suffix+"Left3.PNG"))
    #Left.append(pygame.image.load(Suffix+"Left4.PNG"))
    #Left.append(pygame.image.load(Suffix+"Left5.PNG"))
    #Left.append(pygame.image.load(Suffix+"Left6.PNG"))
    Up=AddTransparency(Up)
    Down=AddTransparency(Down)
    Right=AddTransparency(Right)
    Left=AddTransparency(Left)
    if (atk):
        atkLeft=pygame.image.load(Suffix+"AtkLeft.PNG")
        atkRight=pygame.image.load(Suffix+"AtkRight.PNG")
        atkDown=pygame.image.load(Suffix+"AtkDown.PNG")
        atkUp=pygame.image.load(Suffix+"AtkUp.PNG")
        atkLeft=AddTransparency(atkLeft)
        atkRight=AddTransparency(atkRight)
        atkDown=AddTransparency(atkDown)
        atkUp=AddTransparency(atkUp)
        imgs={"UP":Up,"DOWN":Down,"RIGHT":Right,"LEFT":Left,"ATK_LEFT":atkLeft,"ATK_RIGHT":atkRight,"ATK_UP":atkUp,"ATK_DOWN":atkDown}
    else:
        imgs={"UP":Up,"DOWN":Down,"RIGHT":Right,"LEFT":Left}

    return imgs


def LoadBackgroundImage(zoneParam="testArea"):
    backgroundSuffix="zones/"+zoneParam+"/Background/"
    background=pygame.image.load(backgroundSuffix+"Background.png")
    return background

def LoadTile(zoneParam):
    pass
