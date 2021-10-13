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
    parachute_status()
    return self.parachute
    

def check_letter(self, letter, parachute):
    self.letter = letter
    if self.letter == True:
        parachute
    elif self.letter == False:
        parachute.pop[0]
    return parachute
    

def parachute_status(self, parachute):
    if bool(parachute):
        return self.happy_person
    else:
        return self.sad_person








