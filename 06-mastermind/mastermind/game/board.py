class Board:
    """
    creates a string for the board that will appear on the screen
    """

    #defines the attributes for the board class
    def __init__(self):
        self.board = []
        self.message = ""
        
    #sets board equal to the list so it can be printed
    def define_board(self, num_players, players, guess_list, correct):
        for x in range(num_players + 2):
            if x == 0 or x == num_players + 1:
                one = "-" * 20
            else:
                if not guess_list:
                    guess_list = "----"
                    one = "Player {}: {}, {}" .format(players[x-1], guess_list[x-1], correct)
                else:
                    one = "Player {}: {}, {}" .format(players[x-1], guess_list[x-1], correct)
            self.board.append(one)
        return self.board 

    #sets message equal to a string using current_player from the switch class
    def define_message(self, current_player):
        self.message = "{}'s turn : " .format(current_player)
    
