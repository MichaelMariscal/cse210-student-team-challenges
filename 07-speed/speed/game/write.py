from game.actor import Actor
from game.point import Point

class Write(Actor):
    """
    Take input from user
    """
    def __init__(self):
        super().__init__()

        position = Point(0,370)
        self.set_position(position)
        self.set_text("Buffer: ")

    def user_typing(self, user_input):
        self.set_text(f"Buffer: {user_input}")

    def clear_buffer(self, is_correct, user_input):
        if is_correct:
            user_input.clear()

    