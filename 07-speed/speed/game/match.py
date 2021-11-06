from game.display import Display
from game.actor import Actor
from game.point import Point

class Match(Actor):
    """
    
    """
    def __init__(self):
        self.screen_list = []
        self.words = []
        
        #position = Point(1, constants.MAX_Y)

    def check_word(self, letter):
         _screen_list = [{self.screen_list}]
         all_text = input(" ")
         for item in _screen_list:
             if item in all_text:
                 print("")
         

    def is_match(self, user_text, word):
        if word in user_text:
            return True
        else:
            return False
         
         
         
         #matches = [FALSE]*len

    #def check_word(self, text)
    #if text != "*":
        #self._text += text
        #self._buffer.set_text = text
    #else:
        #self._text = "Buffer: "
        #self._buffer.set_text()
    
   # def is_match(self, user_text, word):
    #    return False
        # we need to get the text out of the word and compare with that text.


    #def add_points(self,points):
        #self._points += points
        #self.set_text(f"Score: {self._points}")

    #def add_points(self,points):
        #self._points += points
        #self.set_text(f"Score: {self._points}")
        #int._points = len(word)

    #def grab_word(self):
            #return self.words




 #if self._buffer in self.screen_list:
 #clear buffer
# How to set position for the score on the top left
#int.point = len(word)
#match = self.screen_list()
#if self.screen_list == True: