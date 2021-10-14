#import modules/classes
import random
class Guesser():
    """

    """
    def __init__(self):
        self.random_word = ["sword", "stock", "dozen", "guard", "trade", "major", "vague", "wreck"]
        self.letter_guess = ""
        self.store_letter = ""
        self.word = random.choice(self.random_word)
        self.guess = ""
        

    def get_guess(self):
        countLetter = len(self.word)
        count = 1
        limit = 5
        choice1 = ("Do you want to add another letter if possible? (y/n):")
        choiceY = ("y")
        choiceN = ("n")

        letter_guess = input("Input {}" .format(count))

        if letter_guess in self.word:
            message ="Correct!"
            print (input(choice1))
        else :
            message = "Incorrect"
            
        if choice1 == choiceY:
            print(input("Select a letter A-Z"))
        else: 
            print (letter_guess)
            self.store_letter += letter_guess
            count +=1

    def display(self):
        blanks = '_' * len(self.word)
        for i in self.word:
            if self.word in letter_guess:
                blanks = blanks[i] + self.word[i] + blanks [i+1:]

        for letter in blanks:
            print(letter, end= '')
        print()


    def get_guess(self):
        self.guess = input("Select a letter A-Z: ")

#How should I go about having the system checking to see if they had the correct letter.