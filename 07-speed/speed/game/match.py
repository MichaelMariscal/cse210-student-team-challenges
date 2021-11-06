from game.display import Display
from game.actor import Actor
from game.point import Point

class Match(Actor):
    """
    Determines if the word is in user_input to signify a match or not.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Match): An instance of Match.
        """
        pass
         

    def is_match(self, user_text, word):
        """Determines match and returns boolean.
        
        Args:
            self (Match): An instance of Match.
            string (word): The word on screen.
            string (user_text): The user's input.
        """
        if word in user_text:
            return True
        else:
            return False
         
         
         
       