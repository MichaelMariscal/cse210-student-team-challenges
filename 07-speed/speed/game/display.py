from game import constants
from game.actor import Actor
from game.point import Point
import random

class Display(Actor):
    """
    Display words going across the screen, control velocity and position.
    """
    def __init__(self):
        super().__init__()
        self.word_list = []
        self.word = ""
        self.X = constants.MAX_X
        self.Y = constants.MAX_Y
        self.prepare_game()

    def prepare_game(self):
        for word in range(5):
            self.choose_word()
            self.word = self._text
            self.set_position()
            self.set_velocity()


    def choose_word(self):
        self.word = random.choice(constants.LIBRARY)

    def control_list(self, word):
        range_x = (1,self.X)
        range_y = (1, self.Y)
        if word in range_x and word in range_y:
            self.word_list.append(word)
        else:
            self.word_list.pop(word)


    def set_position(self):
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y -2)
        position = Point(x,y)
        self.set_position(position)

    def set_velocity(self):
        pass


    
        