from game.console import Console
from game.jumper import Jumper
from game.guesser import Guesser

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        guesser (Guesser)): An instance of the class of objects known as Guesser.
    """

    def __init__(self):
        """
        The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.guesser = Guesser()
        
        
    def start_game(self):
        """
        Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("-------------------------------------------------------------")
        self.guesser.convert_word_to_list()
        self.guesser.return_new_line()
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.jumper.person_status() 
            self.is_game_over()
            if self.keep_playing == True: 
                self.guesser.guess_whole_word()
                if self.guesser.whole_word == False:
                    self.keep_playing = True
                elif self.guesser.whole_word == True:
                    self.keep_playing = False
            

        print("-------------------------------------------------------------")

    def get_inputs(self):
        """
        Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        print()
        self.console.write_list(self.jumper.parachute)
        self.console.write_list(self.jumper.person)
        self.guesser.update_guess()
        self.guesser.check_list()
        self.guesser.check_guess()
        print()
        self.guesser.return_new_line()

    def do_updates(self):
        """
        Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        letter = self.guesser.letter
        self.jumper.check_letter(letter)
        
        
        
    def is_game_over(self):
        """
        Checks if the game is over or not.
        
        Args:
            self (Director): an instance of Director.
        """
        new_word = ''.join(map(str, self.guesser.blank_list))
        new_guesser = ''.join(map(str, self.guesser.word))

        if self.jumper.person == self.jumper.happy_person and new_word != new_guesser:
            self.keep_playing = True
        elif self.jumper.person == self.jumper.happy_person and new_word == new_guesser:
            print('You won! Congrats on not dying.')
            self.keep_playing = False
        elif self.jumper.person == self.jumper.sad_person:
            self.keep_playing = False
            self.console.write_list(self.jumper.person)
            print('Game over! Better luck next time, thanks for playing :)')
        
        else:
            print('Unknown error occurred. Please close down the game and try again.')
            self.keep_playing = False
        

