from game import constants
from game.actor import Actor
from game.point import Point
from game.word import Word
import random

class Display(Actor):
    """
    Display words going across the screen, control velocity and position.

    Attributes: 
        Actor (class): A class to change words into actors
        screen_list (list): A list to store actors
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor and initializes lists.
        
        Args:
            self (Display): an instance of Display.
        """
        super().__init__()
        self.screen_list = []
        

    def prepare_game(self):
        """Prepares the game by gathering five words to change into actors.

        Args:
            self (Display): An instance of Display.
        """
        for i in range(5):
            self.add_word()          

    def choose_word(self):
        """Randomly chooses a word from word list.
        
        Args:
            self (Display): An instance of Display.
        """
        next_word = random.choice(constants.LIBRARY)
        return next_word

    def control_list(self):
        """Manages screen_list by removing words that are going off the screen.
        
        Args:
            self (Display): An instance of Display.
        """
        remove_words = []
        for word in self.screen_list:
            x1 = word.get_position().get_x()
            if x1 < 5:
                self.move_word(word, remove_words)
        remove_words.clear()


    def move_word(self, word, remove_list):
        """Moves a word from one list to another.
        
        Args:
            self (Display): An instance of Display.
        """
        remove_list.append(word)
        self.screen_list.remove(word)

    
    def move(self):
        """Calls a method in Actor to move word on screen.
        
        Args:
            self (Display): An instance of Display.
        """
        for word in self.screen_list:
            word.move_next()

    def add_word(self):
        """Adds a word to actors as called.
        
        Args:
            self (Display): An instance of Display.
        """
        next_word = self.choose_word()
        w = Word()
        w.set_text(next_word)
        self.screen_list.append(w)
        