class Board:
    """
    creates a string for the board that will appear on the screen
    """
    def __init__(self):
        self.board = []
        self.player_message = ""
        self.guess = "What is your guess? "
        

    def define_board(self, players, code, correct):
        for player in players:
            for x in range(player+2):
                if x == 0 or x == player + 1:
                    one = "-" * 20
                else:
                    one = "Player " + players[x-1] ": " + code ", " + correct
                self.board.append(one)
        return self.board 

    def define_message(self, current_player):
        self.player_message = current_player.title() + "'s turn : "
    
