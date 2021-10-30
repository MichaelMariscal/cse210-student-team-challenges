from game import constants
from game.actor import Actor
from game.point import Point
import random

class Display:
    """
    Display words going across the screen, control velocity and position.
    """
    def __init__(self):
        self.word_list = []
        self.word = ""


    def choose_word(self, file):
        self.word = random.choice(open(file).read().split()).strip()

    
        