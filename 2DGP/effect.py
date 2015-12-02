import random

from pico2d import *


class Effect:
    def __init__(self,x,y):
        self.x,self.y= x,y+50
        self.image= load_image("effect.png")




    def update(self):
        self.y +=2

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-20,self.y-15,self.x+20,self.y+15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

