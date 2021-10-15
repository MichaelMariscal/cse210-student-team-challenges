import random
class Guesser():
    """

    """
    def __init__(self):
        self.random_word = ["sword", "stock", "dozen", "guard", "trade", "major", "vague", "wreck"]
        self.word = random.choice(self.random_word)
        self.guess = "Select a letter A-Z: "
        self.choice = "Do you want to add another letter if possible? (y/n): "
        

    def get_guess(self, guess):
        if guess in self.word:
            message ="Correct!"
        else :
            message = "Incorrect"
        return message
            
    def get_answer(self):
        if choice1 == "y":
            answer ="Select a letter A-Z"
        return answer

    def display(self, guess):
        blanks = '_' * len(self.word)
        for i in self.word:
            if self.word in guess:
                blanks = blanks[i] + self.word[i] + blanks [i+1:]

        for letter in blanks:
            print(letter, end= '')
        print()



#How should I go about having the system checking to see if they had the correct letter.