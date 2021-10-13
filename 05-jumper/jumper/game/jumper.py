#import modules/classes

class Jumper:
    """
    print(" ___")
    print("/___\\")
    print("\\   /")
    print(' \ /')
    print('  0')
    print(' /|\\')
    print(' / \\')


    """
def __init__(self):
    self.parachute = ["  ___"," /___\\", " \\   /", '  \ /']
    self.happy_person = ['   0','  /|\\','  / \\', ' ', '^^^^^^^']
    self.sad_person = ['   X', '  /|\\', '  / \\', ' ', '^^^^^^^']
    self.letter = True
    #self.parachute = []

def parachute(self):
    for piece in self.parachute:
        print(piece)


def check_letter(self, letter):
    self.letter = letter
    if self.letter == True:
        print('Correct')
    elif self.letter == False:
        self.parachute.pop[0]
        print('Better luck next time')
    

def parachute_status(self):
    if bool(self.parachute):
        for piece in self.happy_person:
            print(piece)
    else:
        for piece in self.sad_person:
            print(piece)
            print('Game over! Try again another time and live')









