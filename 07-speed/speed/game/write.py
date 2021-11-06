from game.actor import Actor
from game.point import Point

class Write(Actor):
    """
    Take input from user
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Write): An instance of Write.
        """
        super().__init__()
        self.user_input = ""
        position = Point(3,380)
        self.set_position(position)
        self.set_text("Buffer: ")

    def add_letter(self, letter):
        """Adds the letter from user to string to display on Buffer.
        
        Args:
            self (Write): An instance of Write.
            string (letter): The letters to add to string.
        """
        self.user_input += letter
        self.set_text(f"Buffer: {self.user_input}")

    def clear_buffer(self, is_correct):
        """Determines from boolean to to clear the buffer and empty the user_input string.
        
       Args:
            self (Write): An instance of Write.
            boolean (is_correct): Boolean to determine method.
        """
        if is_correct:
            self.user_input = ""
            self.set_text(f"Buffer: {self.user_input}")
