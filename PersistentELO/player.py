import math

class Player(object):

    """Creates a Player Object

    Arguments:

    name (string) - the name of the player
    rating (float) - the initial rating of the player, default to 1200.00
    wins (int) - the initial number wins of the player, default to 0
    losses (int) - the initial number of losses of the player, default to 0
    draws (int) - the initial number of draws of the played, default to 0

    Usage:

    >>>p = Player('Bob') #Player named Bob

    or

    >>>p = Player('Bob',2000.0) #Player named Bob with rating 2000.0


    Notes:

    The name must be unique to the ranking system.

    Rating can be input as an int, it is cast to a float upon initialization

    """

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
        return math.round(self.rating)

    def __str__(self):
        return """\t\tPlayer: %s \n
                Rating: %0.2f\n
                Record: %d-%d-%d""" % \
                (self.name,self.rating,self.wins,self.losses,self.draws)

    __repr__ = __str__