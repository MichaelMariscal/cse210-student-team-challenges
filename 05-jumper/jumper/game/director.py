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
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.guesser = Guesser()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guesser.convert_word_to_list()
        self.console.write(self.guesser.blank_list)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
        self.console.write(self.jumper.sad_person)

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        
        self.console.write_list(self.jumper.parachute)
        self.console.write_list(self.jumper.happy_person)
        self.guesser.update_guess()
        self.guesser.check_guess(self.update_guess.self.guess)
        self.guesser.check_list(self.guesser.update_guess)
        self.guesser.return_new_line(self.guesser.store_letters)
        #self.guesser.return_new_line(self.guesser.check_guess.self.blank_list)

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        guess = self.console.read(self.guesser.guess)
        letter = self.guesser.check_guess(guess)
        self.jumper.check_letter(letter)
        self.jumper.person_status()
    

#    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        

