import pygame
from pygame.math import Vector2 as Vector2

#Setting the title of the game
pygame.display.set_caption("Pac-Man")

#setting the icon of the game
programIcon = pygame.image.load('pacman.png')
pygame.display.set_icon(programIcon)

#screen settings
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER

ROWS = 30
COLS = 30

#colour settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

#font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'