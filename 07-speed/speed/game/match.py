from game.display import Display
from game.actor import Actor
from game.point import Point
class Match(Actor):
    
    
    def __init__(self):
        self.screen_list = []
        self.get_text = ""
        self.words = []
        self._points = 0
        self.set_text(f"Score: {self._points}")
        self.set_text(f"Buffer: {self.words}")
        position = Point(1, constants.MAX_Y)



    def check_word(self, letter):
         self.words += letter
         self.set_text(f"Buffer: {self.words}")
   




    def add_points(self,points):
        self._points += points
        self.set_text(f"Score: {self._points}")
        #int.point = len(word)

    #def grab_word(self):
            #return self.words




 #if self.get_text in self.screen_list:
# How to set position for the score on the top left
#int.point = len(word)
#match = self.screen_list()
#if self.screen_list == True: