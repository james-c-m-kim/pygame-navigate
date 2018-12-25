import sys
import pygcurse
import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *

FPS = 60


def main():
        win = pygcurse.PygcurseWindow(80,40)

        pygame.display.set_caption('Testing This App')

        clock = pygame.time.Clock()

        win.fill('.', fgcolor='yellow', bgcolor='blue')
        win.pygprint('What is your name?')
        win.cursor = (30,20)
        name = win.input()

        win.fill('.', fgcolor='yellow', bgcolor='blue')
        win.colors = ('red', 'yellow')
        win.putchars('Hello, {}!\n'.format(name), x=30, y=22, fgcolor='red', bgcolor='yellow')
        win.putchars('It is good to see you!', x=30, y=24, fgcolor='red', bgcolor='yellow')
        win.putchars('Press SPACE to start, ESC to quit.', x=30, y=24, fgcolor='red', bgcolor='yellow')

        current_x = 30
        current_y = 30

        while True:
            current_x, current_y = handle_events(win, clock, current_x, current_y)
            clock.tick(FPS)


def handle_events(win, clock, current_x, current_y):

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('red', 'yellow')
            win.putchars('BYE!!!', x=30, y=22, fgcolor='red', bgcolor='yellow')
            clock.tick(2000)
            terminate()
        if event.type == KEYDOWN and event.key == K_UP:
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('green', 'red')
            current_y = current_y - 1
            win.putchars('X', x=current_x, y=current_y, fgcolor='green', bgcolor='red')
            win.putchars('x: {}, y: {}'.format(current_x, current_y), x=0, y=0)
            win.update()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('green', 'red')
            current_y = current_y + 1
            win.putchars('X', x=current_x, y=current_y, fgcolor='green', bgcolor='red')
            win.putchars('x: {}, y: {}'.format(current_x, current_y), x=0, y=0)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('green', 'red')
            current_x = current_x - 1
            win.putchars('X', x=current_x, y=current_y, fgcolor='green', bgcolor='red')
            win.putchars('x: {}, y: {}'.format(current_x, current_y), x=0, y=0)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('green', 'red')
            current_x = current_x + 1
            win.putchars('X', x=current_x, y=current_y, fgcolor='green', bgcolor='red')
            win.putchars('x: {}, y: {}'.format(current_x, current_y), x=0, y=0)
        elif event.type == KEYDOWN and event.key == K_SPACE:
            win.fill('.', fgcolor='yellow', bgcolor='blue')
            win.colors = ('green', 'red')
            win.putchars('x: {}, y: {}'.format(current_x, current_y), x=0, y=0)
            win.putchars('X', x=current_x, y=current_y, fgcolor='green', bgcolor='red')

    return current_x, current_y


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

