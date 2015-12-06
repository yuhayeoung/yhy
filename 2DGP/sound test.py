import random
from pico2d import *





def test_ui():
    open_canvas(384,512)
    sound=Sound()
    sound.draw()
    sound.update()
    close_canvas()

if __name__ == '__main__':
    test_ui()
