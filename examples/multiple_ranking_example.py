from PersistentELO import player,elo,ranking
import os

p_1 = player.Player('p_1')
p_2 = player.Player('p_2')

t = player.Player('Terran')
p = player.Player('Protoss')
z = player.Player('Zerg')

e = elo.ELO()

#create a ranking for player and for race 
player_ranking = ranking.Ranking(os.path.join(os.getcwd(),'player_ranking'))
race_ranking = ranking.Ranking(os.path.join(os.getcwd(),'race_ranking'))


#add player profiles to player_ranking
player_ranking.add_player(p_1)
player_ranking.add_player(p_2)

#add race profiles to race_ranking
race_ranking.add_player(t)
race_ranking.add_player(p)
race_ranking.add_player(z)

#assume that p_1 is playing Terran and p_2 is playing Zerg and that p_1 wins
e.update_elo(p_1,p_2,(1,0))
e.update_elo(t,z,(1,0))
player_ranking.store_player(p_1)
player_ranking.store_player(p_2)
race_ranking.store_player(t)
race_ranking.store_player(z)