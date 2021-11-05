from game import constants
from game.actor import Actor
from game.point import Point
from game.word import Word
import random

class Display(Actor):
    """
    Display words going across the screen, control velocity and position.
    """
    def __init__(self):
        super().__init__()
        self.screen_list = []
        

    def prepare_game(self):
        for i in range(5):
            self.add_word()          

    def choose_word(self):
        next_word = random.choice(constants.LIBRARY)
        return next_word

    def control_list(self):
        for word in self.screen_list:
            x1 = word.get_position().get_x()
            if x1 < 5:
                #self.move_word(word)
                #self.remove_word(word)
                pass


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
        w = Word()
        w.set_text(next_word)
        self.screen_list.append(w)
        