import player, elo, pickle

class Ranking(object):
    def __init__(self,data):
        self.elo = elo.ELO()
        self.data = data
        self.players = []

        '''
        load all players from data, get info, put into array
        '''