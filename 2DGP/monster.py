import random

from pico2d import *


class Monster:
    def __init__(self):
        self.x,self.y= 192 ,70
        self.frame = 0
        self.image= load_image("monster_stage1.png")

    def update(self):
        self.frame = (self.frame+1)%4
        self.y -=1
        if self.y<=-500:
            self.y=520
    def draw(self):
        self.image.clip_draw(self.frame*75,0,75,75,self.x,self.y)
