from game.actor import Actor
import random
from game import constants
from game.point import Point


class Word(Actor):
    """
    Word class will have methods that will randomly set the position and velocity of each word (actor) that passes through.
    It will also hold and set the points assigned to each word for easier access.
    """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor and initializes methods.
        
        Args:
            self (Word): an instance of Word.
        """
        super().__init__()
        self.randomize_position()
        self.randomize_velocity()

    def randomize_position(self):
        """Sets the position of Word.
        
        Args:
            self (Word): An instance of word.
        """
        x = constants.MAX_X
        y = random.randint(1, constants.MAX_Y - constants.DEFAULT_FONT_SIZE)
        position = Point(x,y)
        self.set_position(position)

    def randomize_velocity(self):
        """Sets the velocity of word.
        
        Args:
            self (Word): An instance of Word.
        """
        x_velocity = random.randint(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
        velocity = Point(-x_velocity, 0)
        self.set_velocity(velocity)

    def get_points(self, word):
        """Returns points based off of the length of the word.
        
        Args:
            self (Word): An instance of Word.
            string (word): A word.
        """
        points = len(word)
        return points