#import modules/classes
import random

#declare class
class Guesser():
    """
    A code template for the guesser who looks randomly chooses the word and checks if the guess is right or not. The 
    responsibility of this class of objects is to keep track of the hidden word and guess throughout the game.
    
    Stereotype:
        Information Holder

    Attributes:
        random_word (list): The list of words
        guesses (list): Keeps track of the guesses the user made
        store_letters (list): Holds the letters of the hidden word
        letter (boolean): Boolean to tell whether or not the user loses a line of the parachute or not
        whole_word (boolean): To determine if the game ends when they try guessing the whole word or not
        guess (string): A string to hold the user guess
        word (string): To randomly choose a word from the list of words
        blank_list (list): A list to hold the placeholders for the game.
    """

    def __init__(self):
        """
        Class constructor. Declares and initializes instance attributes.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.random_word = ["sword", "stock", "shark", "shirt", "place", "fishy", "dozen", "guard", "trade", "major", "vague", "wreck"]
        self.word = random.choice(self.random_word)
        self.letter = True
        self.whole_word = False
        self.guesses = []
        self.store_letters = []
        self.guess = ""
        self.blank_list = ['_','_','_','_','_']
        
    
    def update_guess(self):
        """
        Gets and holds the user's guess.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.guess = input('Select a letter from a-z: ')
        

    def check_list(self):
        """
        Checks if guess has already been made before.

        Args:
            self (Guesser): An instance of Guesser.
        """

        if self.guess in self.guesses:
            self.letter = False
            print('Already entered this letter. Please try again.')
        else:
            print('Hmm..let\'s see if you got it right or not...')
            self.letter = True
            self.guesses.append(self.guess)


    def check_guess(self):
        """
        Checks if the user's guess is correct or not

        Args:
            self (Guesser): An instance of Guesser.
        """
        if self.guess in self.store_letters:
            self.letter = True
            indexed_number = self.store_letters.index(self.guess)
            self.blank_list[indexed_number] = self.guess
        else:
            self.letter = False            
        
    def convert_word_to_list(self):
        """
        Converts the hidden word to a list to make it easier to check for correct guesses.

        Args:
            self (Guesser): An instance of Guesser.
        """
        for letter in self.word:
            for char in letter:
                self.store_letters.append(char)

    def return_new_line(self):
        """
        Returns the new line with the potential correct guess.

        Args:
            self (Guesser): An instance of Guesser.
        """
        print()
        for letter in self.blank_list:
                print(letter, end=" ")

    def guess_whole_word(self):
        """
        Gives the option if the user wants to try guessing the whole word or not.

        Args:
            self (Guesser): An instance of Guesser.
        """
        answer = input('Wanna guess the whole word?[y/n] ')
        if answer == 'y'.lower():
            word_guess = input('Guess here: ')
            new_guesser = ''.join(map(str, self.word))
            if word_guess == new_guesser:
                print('Wow! You got it!!! You won, congratulations.')
                print(word_guess)
                self.whole_word = True
            else:
                print('Nice try, time to go back to the game.')
                self.whole_word = False
        elif answer == 'n'.lower():
            print('Alright, let us get back to the game then.')
            self.whole_word = False
        else:
            print('I don\'t recognize that answer. Let\'s go back to the game now.')
            self.whole_word = False