import random
import json
import os

from pico2d import *
from background_map import Background
from character import Character
from effect import Effect
from monster import Monster
import game_framework
import title_state



name = "MainState"

background = None
character = None
effects = []
monster = None


def enter():
    global background,character,effect,monster
    background = Background()
    character = Character()
    monster = Monster()



def exit():
    global background,character,effect,monster
    del(background)
    del(character)
    del(effects)
    del(monster)

def pause():
    pass


def resume():
    pass


def handle_events():

    global character
    global monster
    global effects
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        else:
            character.handle_event(event)

        if event.type==SDL_KEYDOWN and event.key == SDLK_SPACE:
            neweffects = Effect(character.x,character.y)
            effects.append(neweffects)


open_canvas(384,512)



def update():
   background.update()
   character.update()

   for effect in effects:
       effect.update()

   monster.update()



   hide_cursor()

def draw():
    clear_canvas()
    background.draw()
    for effect in effects:
        effect .draw()
    character.draw()
    monster.draw()
    update_canvas()



close_canvas()