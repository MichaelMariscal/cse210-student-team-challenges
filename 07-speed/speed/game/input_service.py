import sys
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is
    to detect player keypresses and translate them into a point representing
    a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _current (Point): The last direction that was pressed.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self.key_string = ""

    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()


    def is_letter(self):
        return raylibpy.get_key_pressed()

 
    def get_letter(self):
        key_int = self.is_letter()
        if key_int != -1:
            self.key_string = chr(key_int)
        return self.key_string
