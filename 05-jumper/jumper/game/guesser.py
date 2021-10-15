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
        self.choice1 = ("Do you want to add another letter if possible? (y/n):")
        self.choiceY = ("y")
        self.choiceN = ("n")

    def get_word(self):
        countLetter = len(self.word)
        count = 1
        limit = 5


        while count < limit:
            self.letter_guess = input("Input {}" .format(count))

            if self.letter_guess in self.word:
                print ("Correct!")
                print (input(self.choice1))
            else :
                print("Incorrect")
                count +=1
            if self.choice1 == self.choiceY:
                print(input("Select a letter A-Z"))
            else: 
                print (self.letter_guess)
                self.store_letter += self.letter_guess
                count +=1
       

    def display(self):
        blanks = '_' * len(self.random_word)
        for i in self.word:
            if self.word in self.letter_guess:
                blanks = blanks[i] + self.random_word[i] + blanks [i+1:]

        for letter in blanks:
            print(letter, end= '')
        print()


    def get_guess(self):
        self.guess = input("Select a letter A-Z: ")

#How should I go about having the system checking to see if they had the correct letter.