from game import constants
from game.actor import Actor
from game.point import Point

class Write:
    """
    Take input from user
    """
    def __init__(self):
        super().__init__()
        self._typing = ""
        position = Point(0,370)
        self.set_position(position)
        self.set_text("Buffer: ")

    def user_typing(self, user_input):
        self.set_text(f"Buffer: {user_input}")

    