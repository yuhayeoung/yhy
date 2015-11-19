import random

from pico2d import *

class Background:
    def __init__(self):
        self.back_frame=0
        self.image=load_image('background_stage1.png')
    def draw(self):
        self.image.clip_draw(0,0,384,512, 192,256+self.back_frame)
        self.image.clip_draw(0,0,384,512, 192,768+self.back_frame)
    def update(self):
        self.back_frame -=0.2
        if self.back_frame <= -512:
            self.back_frame=0