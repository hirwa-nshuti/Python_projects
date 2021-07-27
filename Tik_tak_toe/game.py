"""
The file which holds all code for running the game up
"""

# importing all needed modules
import pygame as pg
import sys
import time
from pygame.locals import *

# Global variables
XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]

# The game Display

# Initializing the game window
pg.init()

# Setting fps manually
fps = 30

CLOCK = pg.time.Clock()

# Building the Display infrastructure
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Loading Images and resizing them
initiating_window = pg.image.load('modified_cover.png')
x_img = pg.image.load('X_modified.png')
y_img = pg.image.load('o_modified.png')

initiating_window = pg.transform.scale(initiating_window, (width, height + 1))
x_img = pg.transform.scale(x_img, (80, 80))
y_img = pg.transform.scale(y_img, (80, 80))