import math

class Player(object):

    def __init__(self,name='player',rating=1200.0,wins=0,losses=0,draws=0):
        self.name = name
        self.rating = float(rating)
        self.wins = wins
        self.losses = losses
        self.draws = draws

    def total_games(self):
        return self.wins+self.losses+self.draws

    def __eq__(self,other):
        return self.rating == other.rating
    
    def __ne__(self,other):
        return self.rating != other.rating
    
    def __lt__(self,other):
        return self.rating < other.rating
    
    def __gt__(self,other):
        return self.rating > other.rating
    
    def __le__(self,other):
        return self.rating <= other.rating
    
    def __ge__(self,other):
        return self.rating >= other.rating
    
    def __int__(self):
        return math.ceil(self.rating)

    def __str__(self):
        return """\t\tPlayer: %s \n
                rating: %0.2f\n
                Record: %d-%d-%d""" % (self.name,self.rating,self.wins,self.losses,self.draws)

    __repr__ = __str__