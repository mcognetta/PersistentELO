# PersistentELO

Library for Persistent ELO rankings. Allows users to have an elo ranking system that persists even if your code is stopped.

https://en.wikipedia.org/wiki/Elo_rating_system

###Player Class:
Used to store information about a player including name, rating, and record.

###ELO Class:
Used to specify the ELO system being used, specifically the k-factor that is being applied. This class holds the code for calculating and updating the ratings of players.

###Ranking Class:
Used to rank players and store them in a database. Also holds the match history of the players involved in this ranking. Note that the rankings are ELO agnostic, so you can apply special ranking rules (like in chess) based on the participating players.

##Code examples:

###Basic:

```python
from PersistentELO import player, elo, ranking

p_1 = player.Player("p_1") #create a player named p_1, everything else is set to default
p_2 = player.Player("p_2", rating = 1400.0, wins = 3, losses = 1, draws = 1)

e = elo.ELO() #ELO with default k-factor of 32

r = ranking.Ranking('test_ranking') #ranking system housed in a subdirectory 'test_ranking'

r.add_player(p_1) #add the players into the ranking system so they are tracked
r.add_player(p_2)

e.update_elo(p_1,p_2,(0,1)) #calculate a loss for p_1 and update p_1 and p_2's profiles

r.store_player(p_1) #store both players and the match record in the ranking's directory
r.store_player(p_2)
r.store_game(p_1,p_2,(0,1))
``` 

###Multiple Simultaneous Rankings
We will consider two players playing each other in StarCraft.

```python
from PersistentELO import player,elo,ranking

p_1 = player.Player('p_1')
p_2 = player.Player('p_2')

t = player.Player('Terran')
p = player.Player('Protoss')
z = player.Player('Zerg')


e = elo.ELO()

player_ranking = ranking.Ranking('player_ranking') #create a ranking for player and for race 
race_ranking = ranking.Ranking('race_ranking')

player_ranking.add_player(p_1)
player_ranking.add_player(p_2)

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
```

###Multiple ELO schemes (like in chess)
```python
from PersistentELO import player,elo,ranking

p_1 = player.Player('p_1')
p_2 = player.Player('p_2')

e_1 = elo.ELO() #k-factor 32
e_2 = elo.ELO(24) #k-factor 24

r = ranking.Ranking('test_ranking')

r.add_player(p_1)
r.add_player(p_2)

#if either p_1 or p_2 are ranked over 2100, use the k-factor 24 system, otherwise use k-factor 32
#https://en.wikipedia.org/wiki/Elo_rating_system#Most_accurate_K-factor

if p_1.rating > 2100 or p_2.rating > 2100:
  e_2.update_elo(p_1,p_2,(1,0))
else:
  e_1.update_elo(p_1,p_2,(1,0))

r.store_player(p_1)
r.store_player(p_2)
r.store_game(p_1,p_2,(1,0))
```
