import math
import player

class ELO(object):
    
    def __init__(self,factor=32):
        self.factor = factor

    def expected_victor(self,player1,player2):
        return player1 if player1 > player2 else player2

    def transformed_rating(self,player):
        return math.pow(10,player.elo/400)

    def expected_score(self,player1,player2):
        p1_transform = self.transformed_rating(player1)
        p2_transform = self.transformed_rating(player2)

        p1_expected = p1_transform/(p1_transform+p2_transform)
        p2_expected = p2_transform/(p1_transform+p2_transform)

        return p1_expected,p2_expected

    def update_elo(self,player1,player2,winner):
        
        p1_expected,p2_expected = self.expected_score(player1,player2)
        
        if player1 is winner:
            player1.elo += self.factor*(1-p1_expected)
            player2.elo += self.factor*(0-p2_expected)
            player1.wins += 1
            player2.losses += 1

        elif player2 is winner:
            player1.elo += self.factor*(0-p1_expected)
            player2.elo += self.factor*(1-p2_expected)
            player1.losses += 1
            player2.wins += 1

        else:
            player1.elo += self.factor*(.5-p1_expected)
            player2.elo += self.factor*(.5-p2_expected)
            player1.draws += 1
            player2.draws += 1

    def __str__(self):
        return "ELO System with k-factor %d" % self.factor

    __repr__ = __str__