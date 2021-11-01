from time import sleep

import raylibpy
from game import constants
from game.display import Display
from game.write import Write
from game.match import Match
from game.score_board import ScoreBoard
from game.input_service import InputService


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._display = Display()
        self._write = Write()
        self._match = Match()
        self._score_board = ScoreBoard()
        self._input_service = InputService()

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        self._display.prepare_game()

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        user_input = self._input_service.get_letter()
        self._write.user_typing(user_input)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        word = ''#insert word here!!!!
        self._display.control_list(word)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """

