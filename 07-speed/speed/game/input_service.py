import sys
from game.point import Point
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
        self._current = Point(1, 0)

    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()

    def get_letter(self):
        key_int = raylibpy.get_key_pressed()

        key_string = None

        if key_int != 1:
            key_string = chr(key_int)
        
        return key_string
