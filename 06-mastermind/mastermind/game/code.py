import random

class Code:
    """
    creates, stores, and edits a secret code for each player
    """
    #defines the attributes for this class
    def __init__(self):
        self.secret = []
        self.correct = []

    #sets a secret code for each player in the game
    def secret_code(self, players):
        for player in players:
            code = random.randint
            self.secret.append(code)
    
    def check_code(self):
        pass

    def is_correct(self):
        passs