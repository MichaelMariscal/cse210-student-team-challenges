from time import sleep
import random

import raylibpy
from game import constants
from game.display import Display
from game.write import Write
from game.match import Match
from game.score_board import ScoreBoard
from game.word import Word


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._display = Display()
        self._write = Write()
        self._match = Match()
        self._score_board = ScoreBoard()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._word = Word()

        

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

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
        letter = self._input_service.get_letter()
        if letter != "":    
            self._write.add_letter(letter)


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        remove_words = []
        self._display.move()
        self.add_words()
        words = self._display.screen_list
        for word in words:
            user_text = str(self._write.user_input)

            input_word = ""
            #self._display.screen_list[word]
            found_match = self._match.is_match(user_text, input_word)
            print(found_match)
            print(input_word)
            print(user_text)
            if found_match:
               points = self._word.get_points(word)
               self._score_board.add_points(points)
               self._write.clear_buffer(True)
               self._display.move_word(word, remove_words)
        remove_words.clear()

        #if we found a match get the points from the word and add them to the scoreboard and clear the buffer and remove the word from the list
        self._display.control_list()

 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._display.screen_list)
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._write)
        self._output_service.flush_buffer()


    def add_words(self):
        wild_card = random.randint(1,100)
        if wild_card < 3:
            self._display.add_word()