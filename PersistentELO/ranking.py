import player
import pickle, glob, os

class Ranking(object):

    """Creates a ranking object.

    Arguments:

    data_dir (string) - The directory where the rankings will be stored.


    Usage Example:

    >>>r = ranking.Ranking('path/to/dir')

    Note:

    If the desired directory does not exist, one will be created
    """

    def __init__(self,data_dir):

        self.data_dir = data_dir
        self.players = []

        '''
        load all players from data, get info, put into array
        '''

        if os.path.exists(data_dir):
            os.chdir(data_dir)
            for f in glob.glob("*.pickle"):
                file = open(f,'rb')
                player_info = pickle.load(file)
                self.players.append(player_info)
                file.close()

        else:
            os.mkdir(data_dir)

    def add_player(self,p):

        """Adds a player to the ranking.

        Arguments:

        p (player object) - The player to add to the ranking

        Useage:

        >>>p = player.Player("name")
        >>>r.add_player(p)

        Note:
        If there already exists a player with the same name,
        the player passed in will not be added.

        """

        if any(x.name == p.name for x in self.players):
            print "Could not add player. There already " \
            "exists a player with the name %s." % (p.name)

        else:

            self.players.append(p)
            
            os.chdir(self.data_dir)

            new_pickle = open('%s.pickle' % p.name,'wb')
            pickle.dump(p,new_pickle)
            new_pickle.close()

    def list_all_loaded_players(self):

        """Prints all players currently loaded into the players list."""

        print "All Loaded Players:\n"
        for p in self.players:
            print p
            print "\n"

    def get_all_loaded_players(self):

        """Returns a list of all loaded player objects"""

        return self.players

    def list_all_players(self):
        """Prints all players stored in the data_dir"""

        self.get_all_players()
        print "\n".join(self.players)

    def get_all_players(self):

        """Returns a list of all players in data_dir

        This method clears the current players list and
        readds all players that are stored in the data_dir.

        It will be slow if there are a large amount of players

        """

        os.chdir(self.data_dir)
        self.players = []

        for f in glob.glob("*.pickle"):
            file = open(f,'rb')
            self.players.append(pickle.load(file))
            file.close()

        return self.players

    def store_player(self,p):

        """Stores a player profile in data_dir"""
        
        os.chdir(self.data_dir)

        file = open('%s.pickle' % p.name,'wb')
        pickle.dump(p,file)
        file.close()

