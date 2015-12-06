
from pico2d import *
import game_framework
import main_state

name = "TitleState"
image = None

class Sound:
    def __init__(self):
        self.bgm = load_music("sound_start.mp3")
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
    def draw(self):
        pass


def enter():
    global image,sound
    image = load_image("title_page.png")
    sound=Sound()

def exit():
    global image,sound
    del(image)
    del(sound)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) ==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.push_state(main_state)


def draw():
    clear_canvas()
    image.draw(192 ,256)
    sound.draw()
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






