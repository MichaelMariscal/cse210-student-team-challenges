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
            self (InputService): an instance of InputService.
            self (OutputService): an instance of OutputService.
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
        self._introduction()
        print("Starting game...")
        self._output_service.open_window("Speed")

        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print()
        print("Game over!")
        print(f'Final score: {self._score_board._points}')
        print()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means setting up the game, and getting words
        on the screen to guess.
        
        Args:
            self (Director): An instance of Director.
        """
        self._display.prepare_game()
    
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the text from user to match.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        if letter != "":    
            self._write.add_letter(letter)


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the words and checking for matches.

        Args:
            self (Director): An instance of Director.
        """
        remove_words = []
        self._display.move()
        self.add_words()

        for word in self._display.screen_list:
            user_text = self._write.user_input
            text = word.get_text()
            found_match = self._match.is_match(user_text, text)
            if found_match:
                points = self._word.get_points(text)
                self._score_board.add_points(points)
                self._write.clear_buffer(True)
                if word in self._display.screen_list:
                    self._display.move_word(word, remove_words)

        self._display.control_list()

 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In this case, that means clearing the screen 
        drawing actors and buffer on screen as well.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._display.screen_list)
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._write)
        self._output_service.flush_buffer()


    def add_words(self):
        """Based off of a random number, this method determines whether or not to add another 
        word to the screen.

        Args:
            self (Director): An instance of Director.
        """
        wild_card = random.randint(1,100)
        if wild_card < 4:
            self._display.add_word()

    def _introduction(self):
        """Introduces the game.

        Args:
            self (Director): An instance of Director.
        
        """
        print()
        print('Welcome to the game of Speed! In this game your typing skills will be challenged and improved.')
        print('Once the game pops up, simply just start typing words in until you get it right. No need to worry about the backspace ;)')
        print('Good luck and have fun!')
        print()
        sleep(10)