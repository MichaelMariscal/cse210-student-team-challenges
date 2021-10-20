class Board:
    """
    creates a string for the board that will appear on the screen
    """

    #defines the attributes for the board class
    def __init__(self):
        self.board = []
        self.message = ""
        self.guess = "What is your guess? "
        
    #sets board equal to the list so it can be printed
    def define_board(self, players, code, correct):
        for player in players:
            for x in range(player+2):
                if x == 0 or x == player + 1:
                    one = "-" * 20
                else:
                    one = "Player " + players[x-1] + ": " + code + ", " + correct
                self.board.append(one)
        return self.board 

    #sets message equal to a string using current_player from the switch class
    def define_message(self, current_player):
        self.message = current_player.capitalize() + "'s turn : "
    
