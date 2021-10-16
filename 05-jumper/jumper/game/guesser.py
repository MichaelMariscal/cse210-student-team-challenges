#import modules/classes
import random

#declare class
class Guesser():
    """

    """
    def __init__(self):
        self.random_word = ["sword", "stock", "dozen", "guard", "trade", "major", "vague", "wreck"]
        self.word = random.choice(self.random_word)
        self.letter = True
        self.guesses = []
        self.store_letters = []
        self.blank_list = ['_','_','_','_','_']
        self.current_guess = ""
        
    
    def update_guess(self):
        self.guess = input('Select a letter from a-z: ')
        
    def check_list(self):
        if self.guess in self.guesses:
            self.letter = False
            print('Already entered this letter. Please try again.')
        else:
            print('Hmm..let\'s see if you got it right or not...')
            self.letter = True
            self.guesses.append(self.guess)


    def check_guess(self):
        if self.guess in self.store_letters:
            self.letter = True
            indexed_number = self.store_letters.index(self.guess)
            self.blank_list[indexed_number] = self.guess
        else:
            self.letter = False            
        
    def convert_word_to_list(self):
        for letter in self.word:
            for char in letter:
                self.guesses.append(char)

    def return_new_line(self):
        print()
        for letter in self.blank_list:
                print(letter, end=" ")

       