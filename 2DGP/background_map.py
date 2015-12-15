import random

from pico2d import *

class Background:
    def __init__(self):
        self.back_frame=0
        self.image=load_image('background_stage3.png')
        self.bgm = load_music("sound_bgm.mp3")
        self.bgm.set_volume(80)
        self.bgm.repeat_play()
    def draw(self):
        self.image.clip_draw(0,0,384,512, 192,256+self.back_frame)
        self.image.clip_draw(0,0,384,512, 192,768+self.back_frame)
    def update(self):
        self.back_frame -=0.2
        if self.back_frame <= -512:
            self.back_frame=0