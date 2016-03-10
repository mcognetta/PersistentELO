import os
import sqlite3 as sqlite
import PersistentELO.player as player

class Ranking(object):

    """Creates a ranking object.

    Arguments:

    data_dir (string) - The directory where the rankings will be stored.


    Usage Example:

    >>>r = ranking.Ranking('path/to/dir')

    Note:

    If the desired directory does not exist, one will be created

    Also creates a match_history.csv file for the ranking system
    that will hold a record of played games.

    """

    def __init__(self, data_dir):

        self.data_dir = data_dir
        self.players = []

        '''
        load all players from data, get info, put into array
        '''

        if os.path.exists(data_dir):
            os.chdir(data_dir)

            db = sqlite.connect('rankings.db')
            cur = db.cursor()

            cur.execute('SELECT * FROM Players')

            data = cur.fetchall()

            for d in data:
                name, rating, wins, losses, draws = d
                self.players.append(player.Player(name, rating, wins, losses, draws))

            db.close()


        else:
            os.mkdir(self.data_dir)
            os.chdir(self.data_dir)

            db = sqlite.connect('rankings.db')
            cur = db.cursor()

            cur.execute('Create TABLE Players(Name TEXT, Rating REAL, Wins INT, Losses INT, Draws INT)')
            db.commit()

            db.close()

            file = open('match_history.csv','wb')
            file.write('p1_name,p1_rating,p2_name,p2_rating,p1_score,p2_score\n')
            file.close()

    def add_player(self, p):

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
        os.chdir(self.data_dir)

        db = sqlite.connect('rankings.db')
        cur = db.cursor()

        cur.execute('SELECT EXISTS(SELECT 1 FROM Players WHERE Name=? LIMIT 1)',(p.name,))
        db.commit()

        exists = cur.fetchone()[0]

        if exists:
            db.close()
            return False

        else:
            cur.execute('INSERT INTO Players VALUES(?,?,?,?,?)',(p.name,p.rating,p.wins,p.losses,p.draws,))
            db.commit()

            db.close()

            self.players.append(p)

            return True

    def get_all_players(self):

        """Prints all players currently in the rankings database"""

        os.chdir(self.data_dir)

        db = sqlite.connect('rankings.db')
        cur = db.cursor()

        cur.execute('SELECT * FROM Players')

        data = cur.fetchall()

        db.close()
        return data

    def store_player(self, p):

        """Updates/Stores a player profile in the rankings database"""

        os.chdir(self.data_dir)

        db = sqlite.connect('rankings.db')
        cur = db.cursor()

        cur.execute('SELECT EXISTS(SELECT 1 FROM Players WHERE Name=? LIMIT 1)',(p.name,))

        exists = cur.fetchone()

        if exists:
            cur.execute('UPDATE Players SET Rating=?,Wins=?,Losses=?,Draws=? WHERE Name=?',
                       (p.rating,p.wins,p.losses,p.draws,p.name))
            db.commit()
            db.close()
            return True

        else:
            db.close()
            return False

    def store_game(self, p1, p2, score):

        """Stores a record of a played game.

        Gets the score of a game and the updated ratings
        of the involved players and writes it to the 
        match_history.csv file in the data_dir.

        """
        os.chdir(self.data_dir)
        file = open('match_history.csv','ab')
        file.write('{},{},{},{},{},{}\n'.format(p1.name,\
                                            p1.rating,\
                                            p2.name,\
                                            p2.rating,\
                                            str(score[0]),\
                                            str(score[1])))
        file.close()
