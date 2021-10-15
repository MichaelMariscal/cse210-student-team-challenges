#import modules/classes
import random

#declare class
class Guesser():
    """

    """
    def __init__(self):
        self.random_word = ["sword", "stock", "dozen", "guard", "trade", "major", "vague", "wreck"]
        self.word = random.choice(self.random_word)
        self.guess = ""
        self.letter = True
        self.guesses = []
        self.store_letters = []
        self.blank_list = ['_','_','_','_','_']
        
    
    def update_guess(self):
        self.guess = input(print('Select a letter from a-z: '))
        self.guesses.append(self.guess)

    def check_list(self, guess):
        if guess in self.guesses:
            self.letter == False
            print('Already entered this letter. Please try again.')
        else:
            self.letter == True
        #return self.letter

    def check_guess(self, guess):
        if guess in self.store_letters:
            self.letter == True
            indexed_number = self.store_letters.index(guess)
            #print(indexed_number)
            self.blank_list[indexed_number] = guess
        else:
            self.letter == False
        #return self.letter                
        
    def convert_word_to_list(self):
        for letter in self.word:
            for char in letter:
                self.store_letters.append(char)

    def return_new_line(self, list):
        for piece in list:
                print(piece, end=" ")

       