import sys,os,random
sys.path.append("%s\\.." % (os.getcwd())) #this seems bad

from PersistentELO import player,ranking,elo


def main():

    '''
    Set up ELO and ranking and create some players
    '''

    e = elo.ELO()
    r = ranking.Ranking("%s\\test_ranking" % os.getcwd())

    p1 = player.Player("p1")
    p2 = player.Player("p2")
    p3 = player.Player("p3")

    '''
    Add players to the rankings
    '''

    print "ADDING PLAYERS:\n"

    r.add_player(p1)
    r.add_player(p2)
    r.add_player(p3)

    print "\n##################################"

    '''
    List currently loaded players (at this point all of them)
    '''

    r.list_all_loaded_players()

    '''
    Unload all the players from the ranking
    '''

    r.players = []

    '''
    Test to see that they are all gone
    '''
    for p in r.players:
        print p
    '''
    Reload all the players
    '''

    r.get_all_players()

    '''
    Test to see that they are all back
    '''


    for p in r.players:
        print p

    '''
    Play a few games randomly
    '''
    scores = [(1,0),(0,1),(.5,.5)]

    for i in range(100):
        score = random.choice(scores)
        e.update_elo(r.players[i%3],r.players[(i+1)%3],score)
        r.store_player(r.players[i%3])
        r.store_player(r.players[(i+1)%3])
    
    for p in r.players:
        print "\n"
        print p


if __name__ == "__main__":

    main()