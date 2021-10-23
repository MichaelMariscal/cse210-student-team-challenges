from game.board import Board
from game.console import Console
from game.code import Code
from game.player import Player
from game.switch import Switch

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.board = Board()
        self.switch = Switch()
        self.code = Code()
        self.console = Console()
        self.num_players = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self.code.keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        self.num_players = int(input("How many people are playing? "))
        for i in range(self.num_players):
            name = self.console.read(f"Enter a name for player {i + 1}: ")
            player = Player(name)
            self.switch.add_player(player)
        self.code.store_code_as_list()
            
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        board = self.board.define_board(self.num_players, self.switch.players, self.code.guess_list, self.code.correct)
        self.console.write_list(board)
        player = self.switch.get_current()
        message = self.board.define_message(player)
        self.console.write(message)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        guess = self.console.read_number(self.code.guess)
        self.code.add_guess(self.switch.players, guess)
        self.code.store_code_as_list()
        self.code.store_guess_as_list(self.num_players)
        self.code.is_correct()
        self.code.make_string()
        self.switch.current()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self.code.secret == self.code.correct:
            winner = self.switch.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self.switch.next_player()
