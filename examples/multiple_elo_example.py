from PersistentELO import player,elo,ranking
import os

p_1 = player.Player('p_1')
p_2 = player.Player('p_2')

#create our first elo with default k-factor 32
e_1 = elo.ELO()

#create our second elo with custom k-factor 24
e_2 = elo.ELO(24)

r = ranking.Ranking(os.path.join(os.getcwd(),'multiple_elo_ranking'))

r.add_player(p_1)
r.add_player(p_2)

'''
if either p_1 or p_2 are ranked over 2100 use the k-factor 24 system,
otherwise use k-factor 32
https://en.wikipedia.org/wiki/Elo_rating_system#Most_accurate_K-factor
'''
if p_1.rating > 2100 or p_2.rating > 2100:
  e_2.update_elo(p_1,p_2,(1,0))
else:
  e_1.update_elo(p_1,p_2,(1,0))

r.store_player(p_1)
r.store_player(p_2)
r.store_game(p_1,p_2,(1,0))