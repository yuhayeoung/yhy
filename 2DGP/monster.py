import random

from pico2d import *


class Monster:
    def __init__(self):
        self.x,self.y= 100,70
        self.frame = 0
        self.image= load_image("monster_stage3.png")


    def update(self):
        self.frame = (self.frame+1)%4
        self.y -=1
        if self.y<=-500:
            self.y=900
    def draw(self):
        self.image.clip_draw(self.frame*75,0,75,75,self.x,self.y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y


    def get_bb(self):
        return self.x-22,self.y-25,self.x+22,self.y+25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())