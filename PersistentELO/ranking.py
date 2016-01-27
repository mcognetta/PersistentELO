import player, elo
import pickle, glob, os

class Ranking(object):

    '''
    Creates a ranking object

    This will create a directory that stores some necessary items including 
    '''

    def __init__(self,data_dir,elo):
        self.elo = elo
        self.data_dir = data_dir
        self.players = []

        '''
        load all players from data, get info, put into array
        '''

        if os.path.exists(data_dir):
            os.chdir(data_dir)
            for f in glob.glob(".pickle"):
                file = open(f,'rb')
                player_info = pickle.load(file)
                self.players.append(player_info)
                file.close()

        else:
            os.mkdir(data_dir)

    def add_player(self,p):

        if any(x.name == p.name for x in self.players):
            print "Could not add player. There already exists a player with the name %s." % (p.name)

        else:

            self.players.append(p)
            
            os.chdir(self.data_dir)

            new_pickle = open('%s.pickle' % p.name,'wb')
            pickle.dump(p,new_pickle)
            new_pickle.close()

    def list_all_loaded_players(self):
        print "All Loaded Players:\n"
        for p in self.players:
            print p
            print "\n"

    def get_all_loaded_players(self):
        return self.players

    def list_all_players(self):
        self.get_all_players()
        print "\n".join(self.players)

    def get_all_players(self):
        os.chdir(self.data_dir)
        self.players = []
        print glob.glob(".pickle")
        for f in glob.glob(".pickle"):
            print f
            file = open(f,'rb')
            self.players.append(pickle.load(file))
            file.close()

        return self.players



