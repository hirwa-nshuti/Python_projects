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


def game_initiating_window():

    screen.blit(initiating_window, (0, 0))

    # Updating display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # Vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + "won !"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, True, (255, 255, 255))

    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw

    # winning rows
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2])
           and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1)*height/3 - height/6),
                         (width, (row + 1)*height / 3 - height / 6),
                         4)
            break

