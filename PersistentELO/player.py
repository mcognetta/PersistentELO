import math

class Player(object):

    def __init__(self,name='player',elo=1200.0,wins=0,losses=0,draws=0):
        self.name = name
        self.elo = elo
        self.wins = wins
        self.losses = losses
        self.draws = draws

    def total_games(self):
        return self.wins+self.losses+self.draws

    def __eq__(self,other):
        return self.elo == other.elo
    
    def __ne__(self,other):
        return self.elo != other.elo
    
    def __lt__(self,other):
        return self.elo < other.elo
    
    def __gt__(self,other):
        return self.elo > other.elo
    
    def __le__(self,other):
        return self.elo <= other.elo
    
    def __ge__(self,other):
        return self.elo >= other.elo
    
    def __int__(self):
        return math.ceil(self.elo)

    def __str__(self):
        return """Player: %s \n
                Elo: %0.2f\n
                Record: %d-%d-%d""" % (self.name,self.elo,self.wins,self.losses,self.draws)

    __repr__ = __str__