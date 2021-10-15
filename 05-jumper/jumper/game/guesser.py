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
        #self.store_letters = []
        self.blank_list = ['_','_','_','_','_']
        self.current_guess = ""
        
    
    def ask_guess(self):
        self.current_guess = input('\nSelect a letter from a-z: ')
 

    def check_list(self):
        if self.current_guess in self.guesses:
            #self.letter == False
            print('Already entered this letter. Please try again.')
        #else:
            #self.letter == True
        #return self.letter
    
    def update_guess(self):
        self.guesses.append(self.current_guess)

    def check_guess(self):
        if self.current_guess in self.word:
            self.letter = True
        else:
            self.letter = False
        #return self.letter  

    def change_list(self):
        if self.letter == True:
            indexed_number = self.guesses.index(self.current_guess)
            #print(indexed_number)
            self.blank_list[indexed_number] = self.current_guess
        else:
            print("Oh, no!")
        
    def convert_word_to_list(self):
        for letter in self.word:
            for char in letter:
                self.guesses.append(char)

    def return_new_line(self, list):
        for piece in list:
                print(piece, end=" ")

       