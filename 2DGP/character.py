import random

from pico2d import *


class Character:
    def __init__(self):
        self.x,self.y=192,50
        self.frame = 0
        self.image= load_image("character.png")

    def update(self):
        self.frame = (self.frame+1)%4


    def handle_event(self,event):
        if event.type==SDL_MOUSEMOTION:
            self.x,self.y=event.x,50

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x,50)

    def get_bb(self):
        return self.x-50,self.y-50,self.x+50,self.y+50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
