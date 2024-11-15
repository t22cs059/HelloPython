import random

class Player:
    def init(self, name):
        self._name = name
        self._wincount = 0
        
    def show_hand(self):
        return random.randrange(3)
    
    def notify_result(self, result):
        if True == result:
            self._wincount += 1
            
    def get_wincount(self):
        return self._wincount
    
    def get_name(self):
        return self._name