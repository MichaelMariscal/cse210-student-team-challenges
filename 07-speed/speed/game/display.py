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
        self.screen_list = []
        self.remove_list = []
        self.word = ""
        self.prepare_game()

    def prepare_game(self):
        for i in range(5):
            self.choose_word()
            self.word = self._text
            self.screen_list.append(self.word)
            self.randomize_velocity
            self.randomize_position()

    def choose_word(self):
        self.word = random.choice(constants.LIBRARY)

    def control_list(self, word):
        x1 = word.get_x() 
        if x1 < 5:
            self.move_word(word)
            self.remove_word(word)

    def randomize_position(self):
        #another option for x constants.MAX_X - constants.DEFAULT_FONT_SIZE
        x = random.randint(1, 5)
        y = random.randint(1, constants.MAX_Y - constants.DEFAULT_FONT_SIZE)
        position = Point(x,y)
        self.set_position(position)

    def randomize_velocity(self):
        velocity = random.randint(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
        self.set_velocity(velocity)

    def move_word(self, word):
       self.screen_list.remove(word)
       self.remove_list.append(word)

    def remove_word(self, word):
        self.remove_list.remove(word)
        