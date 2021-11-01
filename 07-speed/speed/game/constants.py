import os
MAX_X = 600
MAX_Y = 400
SNAKE_LENGTH = 60

FRAME_RATE = 30

DEFAULT_SQUARE_LENGTH = 20
DEFAULT_FONT_SIZE = 16

MAX_VELOCITY = -5
MIN_VELOCITY = -1

DEFAULT_TEXT_OFFSET = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
