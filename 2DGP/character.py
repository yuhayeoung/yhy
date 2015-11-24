import random

from pico2d import *


class Character:

    PIXEL_PER_METER=(1.0/0.01)      # 1pixel =1cm
    RUN_SPEED_KMPH = 20.0           #km/hour
    RUN_SPEED_MPM=(RUN_SPEED_KMPH *1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
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
        return self.x-30,self.y-50,self.x+30,self.y+50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
