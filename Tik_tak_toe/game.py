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
