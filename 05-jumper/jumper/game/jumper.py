
class Jumper:
    """A code template for the jumper who looks holds the parachute. The 
    responsibility of this class of objects is to keep track of the parachute throughout the game.
    
    Stereotype:
        Information Holder

    Attributes:
        parachute (list): The whole starting parachute
        happy_person (list): The person before the parachute is gone
        sad_person (list): The person after the parachute is gone
        letter (boolean): Boolean to tell whether or not the user loses a line of the parachute or not
        person (list): List to hold a sad_person or happy_person
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
            """
        if letter == True:
            print()
            print()
        elif letter == False:
            print()
            print()
            del self.parachute[0]

    def person_status(self):
        """Determines when the parachute is gone

            Args:
                self (Jumper): An instance of Jumper.
            """
        if len(self.parachute) == 0:
            self.person = self.sad_person
           
        else:
            self.person = self.happy_person
           








