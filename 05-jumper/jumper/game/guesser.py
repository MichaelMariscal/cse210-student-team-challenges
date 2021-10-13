#import modules/classes
import random
class Guesser():
    """

    """
    def __init__(self):
        self.word = random.choice(random_word)
        self.guess = ""
        pass

    def get_word(self):
        random_word = [sword, stock, dozen, guard, trade, major, vague, wreck ]
        letter_guess = ""
        store_letter = ""
        countLetter = len(word)
        count = 1
        limit = 5
        while count < limit:
            letter_guess = input("Input {}" .format(count))

        if letter_guess in word:
            print ("Correct!")
            print (input(choice1))
        else :
            print("no")
            count +=1
    

    def get_guess(self):
        self.guess = input("Select a letter A-Z: ")

#How should I go about having the system checking to see if they had the correct letter.