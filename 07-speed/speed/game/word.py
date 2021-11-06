from game.actor import Actor
import random
from game import constants
from game.point import Point


class Word(Actor):
    """

    """

    def __init__(self):
        super().__init__()
        self.randomize_position()
        self.randomize_velocity()

    def randomize_position(self):
        #another option for x constants.MAX_X - constants.DEFAULT_FONT_SIZE
        x = constants.MAX_X
        y = random.randint(1, constants.MAX_Y - constants.DEFAULT_FONT_SIZE)
        position = Point(x,y)
        self.set_position(position)

    def randomize_velocity(self):
        x_velocity = random.randint(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
        velocity = Point(-x_velocity, 0)
        self.set_velocity(velocity)

    def get_points(self, word):
        points = len(word)
        return points