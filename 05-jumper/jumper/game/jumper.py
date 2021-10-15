
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
    print(" ___")
    print("/___\\")
    print("\\   /")
    print(' \ /')
    print('  0')
    print(' /|\\')
    print(' / \\')


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
        #self.parachute = []

    """
    def parachute(self):
        Gets a message from the seeker.

            Args:
                self (Jumper): An instance of Jumper.
            
            Returns:
                string: The parachute.
            
        parachute = check_letter()
        return parachute
        
    """
    def check_letter(self, letter):
        """Checks if they lose a line of the parachute or not.

            Args:
                self (Jumper): An instance of Jumper.
            
            Returns:
                string: New parachute.
            """
        self.letter = letter
        if letter == True:
            self.parachute
        elif letter == False:
            self.parachute.pop[0]
        return self.parachute
        

    def person_status(self):
        """Determines if they win or not.

            Args:
                self (Jumper): An instance of Jumper.
                parachute(string):
            Returns:
                string: Person on parachute
            """
        if bool(self.parachute):
            return self.happy_person
        else:
            return self.sad_person








