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
        self.word = Actor()
        self.prepare_game()

    def prepare_game(self):
        for i in range(5):
            self.add_word()          

    def choose_word(self):
        next_word = random.choice(constants.LIBRARY)
        return next_word

    def control_list(self):
        for word in self.screen_list:
            x1 = self.word.get_position().get_x()
            if x1 < 5:
                self.move_word(word)
                self.remove_word(word)

    def randomize_position(self):
        #another option for x constants.MAX_X - constants.DEFAULT_FONT_SIZE
        x = random.randint(1, 5)
        y = random.randint(1, constants.MAX_Y - constants.DEFAULT_FONT_SIZE)
        position = Point(x,y)
        self.word.set_position(position)

    def randomize_velocity(self):
        x_velocity = random.randint(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
        velocity = Point(-x_velocity, 0)
        self.word.set_velocity(velocity)

    def move_word(self, word):
       self.screen_list.remove(word)
       self.remove_list.append(word)

    def remove_word(self, word):
        self.remove_list.remove(word)
    
    def move(self):
        for word in self.screen_list:
            word.move_next()

    
    def add_word(self):
        next_word = self.choose_word()
        self.word.set_text(next_word)
        self.randomize_velocity()
        self.randomize_position()
        self.screen_list.append(self.word)