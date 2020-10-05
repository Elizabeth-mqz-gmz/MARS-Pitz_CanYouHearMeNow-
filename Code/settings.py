import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 600
HEIGHT = 600
FPS = 60
TITLE = "Mars Odyssey"
BGCOLOR = LIGHTGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300
PLAYER_IMG = 'manBlue_hold.png'
PLAYER_ROTATION_SPEED = 250
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)