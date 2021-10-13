#import modules/classes
import random
class Guesser():
    """

    """
    def __init__(self):
        self.word = random.choice(random_word)
        self.guess = ""
        

    def get_word(self):
        random_word = [sword, stock, dozen, guard, trade, major, vague, wreck ]
        letter_guess = ""
        store_letter = ""
        countLetter = len(word)
        count = 1
        limit = 5
        choice1 = ("Do you want to add another letter if possible? (y/n):")
        choiceY = ("y")
        choiceN = ("n")

    while count < limit:
        letter_guess = input("Input {}" .format(count))

        if letter_guess in word:
            print ("Correct!")
            print (input(choice1))
        else :
            print("Incorrect")
            count +=1
        if choice1 == choiceY:
            print(input("Select a letter A-Z"))
        else: 
            print (letter_guess)
            store_letter += letter_guess
            count +=1

    def display(self):
        blanks = '_' * len(random_word)
        for letter_guess in random_word:
            if random_word in letter_guess:
                blanks = blanks[:i] + random_word[i] + blanks [i+1:]

        for letter in blanks:
            print(letter, end= '')
        print()


    def get_guess(self):
        self.guess = input("Select a letter A-Z: ")

#How should I go about having the system checking to see if they had the correct letter.