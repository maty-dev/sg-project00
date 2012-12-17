# -*- coding: utf-8 *-*
import pygame,components
from pygame.locals import *


class Player(components.Entity):

    def __init__(self,images):
        components.Entity.__init__(self,images)
        self.values=[]

    def Update(self,events,background):
        move=components.MoveFunctions()
        self.values=move.CompleteMove(events)
        self.imageDef=self.values[2]
        self.isMoving=self.values[3]

    def Animation(self,time):
        if(self.isMoving and time==1):
            self.pos+=1
            if (self.pos>(len(self.anim[self.imageDef])-1)):
                self.pos=0
        self.image=self.anim[self.imageDef][self.pos]

