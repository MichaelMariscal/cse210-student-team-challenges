from game.actor import Actor
from game.point import Point

class Write(Actor):
    """
    Take input from user
    """
    def __init__(self):
        super().__init__()
        self.user_input = ""
        position = Point(0,380)
        self.set_position(position)
        self.set_text("Buffer: ")

    def add_letter(self, letter):
        self.user_input += letter
        self.set_text(f"Buffer: {self.user_input}")

    def clear_buffer(self, is_correct):
        if is_correct:
            self.user_input = ""
            self.set_text(f"Buffer: {self.user_input}")
