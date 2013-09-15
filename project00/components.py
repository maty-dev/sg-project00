# -*- coding: utf-8 *-*
import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):

    def __init__(self,image,scrolling=False):
        self.image=image
        self.scrolling=scrolling
        self.rect=self.image.get_rect()

    def Update(self,x,y):
        if(self.scrolling):
            self.rect.move_ip(-x,-y)

    def Render(self,screen):
        screen.blit(self.image,self.rect)

class Pointer(pygame.rect.Rect):

    def __init__(self):
        pygame.rect.Rect.__init__(self,0,0,1,1)

    def Update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):

    def __init__(self,images,x,y):
        self.anim=images
        self.imageDef=0
        self.image=self.anim[self.imageDef]
        self.rect=self.image.get_rect()
        self.rect.top=x
        self.rect.left=y

    def Update(self,click=False):
        if (pointer.rect.colliderect(self.rect)):
            self.image=self.anim[(self.imageDef+1)]
        if(click):
            self.image=self.anim[(self.imageDef+2)]
        else:
            self.image=self.anim[(self.imageDef)]

    def Render(self,screen):
        screen.blit(self.image,self.rect)

class Entity(pygame.sprite.Sprite):

    def __init__(self,images,x=200,y=200):
        self.anim=images
        self.imageDef="DOWN"
        self.attackImage="ATK_DOWN"
        self.pos=0
        self.image=self.anim[self.imageDef][self.pos]
        self.rect=self.image.get_rect()
        self.rect.top,self.rect.left=(x,y)
        self.isMoving=False
        self.isAttacking=False
        self.rightKDown=False
        self.leftKDown=False
        self.upKDown=False
        self.downKDown=False
        self.speed=10
        self.x=0
        self.y=0
        self.type="Entity"

    def Update(self,events):
        pass

    def Render(self,screen):
        screen.blit(self.image,self.rect)

    def IsType(self,pType):
        if(pType==self.type):
            return True
        else:
            return False

class Item(Entity):

<<<<<<< HEAD
    def __init__(self):
        super(Item, self).__init__()
        self.type="Item"
        self.image=None

    def StoreItem():
        return None
=======
    def __init__(self,images):
        super(Item, self).__init__()
        self.type="collectable"


class Zone():

    def __init__(self,imLoader,zoneType="testArea"):
        self.type=zoneType
        self.background
        self.items={}
        self.enemies={}
        self.tiles={}
        self.imgLoader=imLoader

    def Load():
        self.background=Background(imgLoader.LoadBackgroundImage(self.type,True))

    def GenerateItems():
        pass


class Map():

    def __init__(self,zoneParam):
        self.zone=zoneParam
        self.tiles=zoneParam.tiles
>>>>>>> 8eb61447ba854a487814af399bef19508daf1e0d
