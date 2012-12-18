# -*- coding: utf-8 *-*
import pygame,components
from pygame.locals import *


class Player(components.Entity):

    def __init__(self,images):
        components.Entity.__init__(self,images)

    def Update(self,events,time):
        if(self.x==0 and self.y==0):
            self.isMoving=False
        self.values=self.Move(events)
        if(self.isMoving and time==1):
            self.Animation()

    def Move(self,events):
        isMoving=False
        for event in events:
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_RIGHT):
                    self.rightKDown=True
                    self.imageDef="RIGHT"
                    self.x=self.speed
                    self.isMoving=True
                if(event.key==pygame.K_LEFT):
                    self.leftKDown=True
                    self.imageDef="LEFT"
                    self.x=-self.speed
                    self.isMoving=True
                if(event.key==pygame.K_UP):
                    self.upKDown=True
                    self.imageDef="UP"
                    self.y=-self.speed
                    self.isMoving=True
                if(event.key==pygame.K_DOWN):
                    self.downKDown=True
                    self.imageDef="DOWN"
                    self.y=self.speed
                    self.isMoving=True
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_RIGHT):
                    if(self.leftKDown):
                        self.x=-self.speed
                    else:
                        self.x=0
                    self.rightKDown=False
                if(event.key==pygame.K_LEFT):
                    if(self.rightKDown):
                        self.x=self.speed
                    else:
                        self.x=0
                    self.leftKDown=False
                if(event.key==pygame.K_UP):
                    if(self.downKDown):
                        self.y=self.speed
                    else:
                        self.y=0
                    self.upKDown=False
                if(event.key==pygame.K_DOWN):
                    if(self.upKDown):
                        self.y=-self.speed
                    else:
                        self.y=0
                    self.downKDown=False

    def Animation(self):
            self.pos+=1
            if (self.pos>(len(self.anim[self.imageDef])-1)):
                self.pos=0
            self.image=self.anim[self.imageDef][self.pos]

