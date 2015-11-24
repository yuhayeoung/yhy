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
monsters = []

running = True
global current_time
global frame_time


current_time = 0.0


def enter():
    global background,character,effect,monsters
    background = Background()
    character = Character()
    #수정 필요
    monsters = create_monster_team()



def exit():
    global background,character,effect,monster
    del(background)
    del(character)

def pause():
    pass


def resume():
    pass


def create_monster_team():


    team = []
    #아몰랑 여따 하드 코딩 하시길
    #monster(숫자 지정) = Monster()
    #monster(지정한 숫자).set_pos(x값, y값)
    #team.append(monster(지정한 숫자))
    monster1=Monster()
    monster1.set_pos(38.4*1, 900)
    team.append(monster1)

    monster2=Monster()
    monster2.set_pos(38.4*3, 900)
    team.append(monster2)

    monster3=Monster()
    monster3.set_pos(38.4*5, 900)
    team.append(monster3)

    monster4=Monster()
    monster4.set_pos(38.4*7, 900)
    team.append(monster4)

    monster5=Monster()
    monster5.set_pos(38.4*9, 900)
    team.append(monster5)


    return team


def handle_events():

    global character

    global effects
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        else:
            character.handle_event(event)

        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
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

   for monster in monsters:
        monster.update()

   #몬스터 재생성 구현되면 활성화
   #for monster in monsters:
   #    if monster.y <=0:
   #        monsters.remove(monster)

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
    character.draw()

    for effect in effects:
        effect .draw()

    for monster in monsters:
        monster.draw()

    update_canvas()



close_canvas()