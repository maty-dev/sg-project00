# -*- coding: utf-8 *-*
import pygame,components
from pygame.locals import *


class Player(components.Entity):

    def __init__(self):
        components.Entity.__init__(self,images,x,y)
        self.position

    def Update(self,events,background):
        move=components.MoveFunctions()
        self.position=move.CompleteMove(events)
        self.imageDef=self.position[2]
        self.isMoving=self.position[3]

    def Animation(self,time):
        pass
