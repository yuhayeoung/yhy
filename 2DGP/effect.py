import random

from pico2d import *


class Effect:
    def __init__(self,x,y):
        self.x,self.y= x,y
        self.image= load_image("effect.png")


    def update(self):
        self.y +=2

    def draw(self):
        self.image.clip_draw(0,0,50,50,self.x,self.y)

    def get_bb(self):
        return self.x-25,self.y-25,self.x+25,self.y+25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())