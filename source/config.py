import pygame
from game import *

# Dividing constant on resolution
WINDOW_SCALE = 1.5

# Resolution using on gameplay logic
GAME_WIDTH = 640
GAME_HEIGHT = 360

# Settings
fullscreen = False

def init():
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global GAME_SCALE

    # Max resolution on screen
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h

    GAME_SCALE = SCREEN_WIDTH / GAME_WIDTH

def toggleFullscreen(game):
    global fullscreen
    global WINDOW_SCALE
    if not fullscreen:
        fullscreen = True
        WINDOW_SCALE = 1
        game.resizeScreen()
    else:
        fullscreen = False
        WINDOW_SCALE = 1.5
        game.resizeScreen()
