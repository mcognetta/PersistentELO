import sys,os,random
from PersistentELO import player,ranking,elo

def main():

    '''
    Set up ELO and ranking and create some players
    '''

    e = elo.ELO()
    r = ranking.Ranking(os.path.join(os.getcwd(),'example_ranking'))

    p1 = player.Player("p1")
    p2 = player.Player("p2")
    p3 = player.Player("p3")
    p4 = player.Player("p4")
    p5 = player.Player("p5")
    p6 = player.Player("p6")
    p7 = player.Player("p7")
    p8 = player.Player("p8")
    p9 = player.Player("p9")
    p10 = player.Player("p10")
    p11 = player.Player("p11")
    p12 = player.Player("p12")
    p13 = player.Player("p13")
    p14 = player.Player("p14")
    p15 = player.Player("p15")

    '''
    Add players to the rankings
    '''

    r.add_player(p1)
    r.add_player(p2)
    r.add_player(p3)
    r.add_player(p4)
    r.add_player(p5)
    r.add_player(p6)
    r.add_player(p7)
    r.add_player(p8)
    r.add_player(p9)
    r.add_player(p10)
    r.add_player(p11)
    r.add_player(p12)
    r.add_player(p13)
    r.add_player(p14)
    r.add_player(p15)
    
    '''
    Play a few games randomly
    '''
    scores = [(1,0),(0,1),(.5,.5)]

    for i in range(100):
        player_1,player_2 = random.choice(r.players),random.choice(r.players)
        p1_win_percent = e.expected_score(player_1,player_2)[0]
        rand = random.random()
        if rand < p1_win_percent:
            score = scores[0]
        else:
            score = scores[1]
        e.update_elo(player_1,player_2,score)
        r.store_player(player_1)
        r.store_player(player_2)
        r.store_game(player_1,player_2,score)
    
    print("Current Rankings:")
    for p in sorted(r.players,key=lambda x: x.rating,reverse=True):
        print(p)

if __name__ == "__main__":

    main()