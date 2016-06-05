from PersistentELO import player, elo, ranking
import os

#create a player named p_1, everything else is set to default
p_1 = player.Player("p_1")
#create a player named p_2 with custom starting stats
p_2 = player.Player("p_2", rating = 1400.0, wins = 3, losses = 1, draws = 1)

#ELO with default k-factor of 32
e = elo.ELO()

#ranking system housed in a subdirectory 'test_ranking'
r = ranking.Ranking(os.path.join(os.getcwd(),'basic_example'))

#add the players into the ranking system so they are tracked
r.add_player(p_1)
r.add_player(p_2)

#calculate a loss for p_1 and update p_1 and p_2's profiles
e.update_elo(p_1,p_2,(0,1))

#store both players and the match record in the ranking's directory
r.store_player(p_1)
r.store_player(p_2)
r.store_game(p_1,p_2,(0,1))