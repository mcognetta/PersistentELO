import player, elo
import pickle, glob, os

class Ranking(object):

    '''
    Creates a ranking object

    This will create a directory that stores some necessary items including 
    '''

    def __init__(self,data_dir,elo):
        self.elo = elo.ELO()
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
                #print player_info
                self.players.append(player_info)

        else:
            print "Creating new data directory"
            os.makedir(data_dir)
            '''
            os.chdir(data_dir)
            os.makedir('players')
            os.makedir('list')
            '''

    def add_player(self,p):

        if any(x.name == p.name for x in self.players):
            print "There already exists a player with that name"

        else:

            players.append(p)
            
            os.chdir(data_dir)

            new_pickle = open('%s.pickle' % p.name,'w')
            pickle.dump(player,new_pickle)
            new_pickle.close()

    def list_all_players(self):
        pass