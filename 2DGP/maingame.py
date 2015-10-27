from pico2d import *



class Back_Ground:
    def __init__(self):
        self.back_frame=0
        self.image=load_image('background_image_0.png')
    def draw(self):
        self.image.clip_draw(0,0,384,512, 192,256+self.back_frame)
        self.image.clip_draw(0,0,384,512, 192,768+self.back_frame)
    def update(self):
        self.back_frame -=20
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
        self.y +=20
        if self.y>=512:
            self.y=70
    def draw(self):
        self.image.clip_draw(0,0,50,50,self.x,self.y)



def handle_events():
    global running
    global character
    global effect
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            running = False
        else:
            character.handle_event(event)
            effect.handle_event(event)


open_canvas(384,512)
hide_cursor()
back_ground=Back_Ground()
character=Character()
effect= Effect()
running = True



while (running):
    handle_events()
    back_ground.update()
    character.update()
    effect.update()

    clear_canvas()
    back_ground.draw()
    effect.draw()
    character.draw()
    update_canvas()
    delay(0.1)

close_canvas()




