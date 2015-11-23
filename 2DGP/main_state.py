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

running = True
global current_time
global frame_time


current_time = 0.0


def enter():
    global background,character,effect,monster
    background = Background()
    character = Character()
    monster = Monster()



def exit():
    global background,character,effect,monster
    del(background)
    del(character)
    del(monster)

def pause():
    pass


def resume():
    pass


def create_monster_team():
    team_data_text = '                   \
        {                             \
           "1" : {"x":38.4*1, "y":70},  \
    	    "2" : {"x":38.4*3, "y":70},  \
    	    "3" : {"x":38.4*5, "y":70},  \
    	    "4" : {"x":38.4*7, "y":70},  \
    	    "5" : {"x":38.4*9, "y":70}   \
        }                             \
    '
    team_data = json.load(team_data_text)

    team=[]
    for number in team_data:
        monster=Monster()
        monster.number = number
        monster.x= team_data[number]["x"]
        monster.y= team_data[number]["y"]
        team.append(monster)
    return team


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

        if running==True:
            neweffects = Effect(character.x,character.y)
            effects.append(neweffects)


open_canvas(384,512,sync =True)









def update():
   background.update()
   character.update()
   for effect in effects:
       effect.update()

   for effect in effects:
       if effect.y>=500:
          effects.remove(effect)

   monster.update()

   hide_cursor()

   current_time = get_time()
   frame_time = get_time() - current_time
   if(frame_time != 0):
         frame_rate = 1.0/frame_time
         print("frame rate : %f fps,frame time : %f sec, "%(frame_rate,frame_time))

   current_time += frame_time

def draw():
    clear_canvas()
    background.draw()
    for effect in effects:
        effect .draw()
    character.draw()
    monster.draw()
    update_canvas()



close_canvas()