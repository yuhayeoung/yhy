import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

background = None
character = None
effect = None



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


def enter():
    global background,character,effect
    background = Background()
    character = Character()
    effect = Effect()



def exit():
    global background,character,effect
    del(background)
    del(character)
    del(effect)

def pause():
    pass


def resume():
    pass


def handle_events():

    global character
    global effect
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        else:
            character.handle_event(event)
            effect.handle_event(event)



open_canvas(384,512)
hide_cursor()


def update():
   background.update()
   character.update()
   effect.update()


def draw():
    clear_canvas()
    background.draw()
    effect.draw()
    character.draw()
    update_canvas()



close_canvas()