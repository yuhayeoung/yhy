import random

from pico2d import *


class Effect:
    def __init__(self):
        self.x,self.y= 192 ,70
        self.image= load_image("effect.png")
    def handle_event(self,event):
        if event.type==SDL_MOUSEMOTION:
            self.x=event.x

    def update(self):
        self.y +=2
        if self.y>=512:
            self.y=70
    def draw(self):
        self.image.clip_draw(0,0,50,50,self.x,self.y)
