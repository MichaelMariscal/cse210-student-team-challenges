import random

class Code:
    """
    creates, stores, and edits a secret code for each player
    """
    #defines the attributes for this class
    def __init__(self):
        self.secret = []
        self.correct = ""
        self.store_secret = []
        self.guess_list = []
        self.store_guess = []
        self.guess = "What is your guess? "
        self.store_correct = []

    #sets a secret code for each player in the game
    def secret_code(self, players):
        for player in players:
            code = random.randint(1000,9999)
            self.secret.append(code)
    
    #checks to see if the code is correct*******
    def add_guess(self, players, guess):
        self.guess_list.append(guess)
        for x in players:
            if self.guess_list[x] == False:
                add = "----"
            self.guess_list.append(add)

    #stores the secret code as a list to get it ready to be checked in a list
    def store_code_as_list(self, num_player):
        secret_code = self.secret[num_player]
        for number in secret_code:
            for int in number:
                self.store_secret.append(int)

    #stores the guess in a list that can be used in a loop
    def store_guess_as_list(self,num_player):
        current_guess = self.guess_list[num_player]
        for number in current_guess:
            for int in number:
                self.store_guess.append(int)

    #checks whether or not the code is correct and returns the symbols used for the game
    def is_correct(self):
        for i in range(5):
            if self.store_guess[i] == self.store_secret[i]:
                answer = "*"
            elif self.store_guess[i] in self.store_secret:
                answer = "o"
            else:
                answer = "x"
            self.store_correct.append(answer)

    #sets the list equal to a string to use for the board class
    def make_string(self):
        self.correct = self.store_correct[0] + self.store_correct[1] + self.store_correct[2] + self.store_correct[3]

