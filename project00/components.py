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


class MoveFunctions():

    def __init__(self):
        self.direction="DOWN"
        self.leftKDown=False
        self.rightKDown=False
        self.upKDown=False
        self.downKDown=False
        self.speed=10

    def DefMove(self,events):
        for event in events:
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_RIGHT):
                    x=self.speed
                    self.rightkDown=True
                    self.direction="RIGHT"
                if(event.key==pygame.K_LEFT):
                    x=-self.speed
                    self.leftKDown=True
                    self.direction="LEFT"
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_RIGHT):
                    if (self.leftKDown):
                        x=-self.speed
                    else:
                        x=0
                if(event.type==pygame.K_LEFT):
                    if(self.rightKDown):
                        x=self.speed
                    else:
                        x=0
        return(x,self.direction)

    def CompleteMove(self,events):
        isMoving=False
        x=0
        y=0
        for event in events:
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_RIGHT):
                    self.rightKDown=True
                    self.direction="RIGHT"
                    x=self.speed
                    isMoving=True
                if(event.key==pygame.K_LEFT):
                    self.leftKDown=True
                    self.direction="LEFT"
                    x=-self.speed
                    isMoving=True
                if(event.key==pygame.K_UP):
                    self.upKDown=True
                    self.direction="UP"
                    y=-self.speed
                    isMoving=True
                if(event.key==pygame.K_DOWN):
                    self.downKDown=True
                    self.direction="DOWN"
                    y=self.speed
                    isMoving=True
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_RIGHT):
                    if(self.leftKDown):
                        x=-self.speed
                    else:
                        x=0
                    self.rightKDown=False
                if(event.key==pygame.K_LEFT):
                    if(self.rightKDown):
                        x=self.speed
                    else:
                        x=0
                    self.leftKDown=False
                if(event.key==pygame.K_UP):
                    if(self.downKDown):
                        y=self.speed
                    else:
                        y=0
                    self.upKDown=False
                if(event.key==pygame.K_DOWN):
                    if(self.upKDown):
                        y=-self.speed
                    else:
                        y=0
                    self.downKDown=False
        value=(x,y,self.direction,isMoving)
        return value

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
        self.pos=0
        self.image=self.anim[self.imageDef][self.pos]
        self.rect=self.image.get_rect()
        self.rect.top,self.rect.left=(x,y)
        self.isMoving=False
        self.rightKDown=False
        self.leftKDown=False
        self.upKDown=False
        self.downKDown=False
        self.speed=10
        self.x=0
        self.y=0

    def Update(self,events):
        pass

    def Render(self,screen):
        screen.blit(self.image,self.rect)
