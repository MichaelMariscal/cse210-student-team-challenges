
class Jumper:
    """A code template for the jumper who looks holds the parachute. The 
    responsibility of this class of objects is to keep track of the parachute throughout the game.
    
    Stereotype:
        Information Holder

    Attributes:
        parachute (list): The whole starting parachute
        happy_person (list): The person before the parachute is gone
        sad_person(list): The person after the parachute is gone
        letter(boolean): Boolean to tell whether or not the user loses a line of the parachute or not
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

            Args:
                self (Jumper): An instance of Jumper.
            """
        self.parachute = ["  ___"," /___\\", " \\   /", '  \ /']
        self.happy_person = ['   0','  /|\\','  / \\', ' ', '^^^^^^^']
        self.sad_person = ['   X', '  /|\\', '  / \\', ' ', '^^^^^^^']
        self.letter = True
        self.person = ['   0','  /|\\','  / \\', ' ', '^^^^^^^']


    def check_letter(self, letter):
        """Checks if they lose a line of the parachute or not.

            Args:
                self (Jumper): An instance of Jumper.
            
            Returns:
                string: New parachute.
            """
        if letter == True:
            print()
            print()
        elif letter == False:
            print()
            print()
            self.parachute.pop()[0]
        

    def person_status(self):
        """Determines if they win or not.

            Args:
                self (Jumper): An instance of Jumper.
                parachute(string):
            Returns:
                string: Person on parachute
            """
        if len(self.parachute) == 0:
            self.person = self.sad_person
           
        else:
            self.person = self.happy_person
           








