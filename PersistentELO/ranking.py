import player, elo
import pickle, glob, os

class Ranking(object):
    def __init__(self,data_dir):
        self.elo = elo.ELO()
        self.data_dir = data_dir
        self.players = []

        '''
        load all players from data, get info, put into array
        '''

        if os.path.exists(data_dir):
            os.chdir(data_dir)
            for f in glob.glob(".pickle"):
                file = open(f,'r')
                player_info = pickle.load(file)
                #print player_info
                self.players.append[player_info]

        else:
            print "Creating new data directory"
            os.makedir(data_dir)

    def add_player(self,player):
        pass