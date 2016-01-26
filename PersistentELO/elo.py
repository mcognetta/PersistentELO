import math
import player

class ELO(object):
    
    def __init__(self,k_factor=32):
        self.k_factor = k_factor

    def expected_victor(self,player1,player2):
        '''
        Returns the player with the higher elo
        as that player is expected to win.

        In the event of both players having the same elo,
        it returns the first parameter player.
        '''
        return player1 if player1 >= player2 else player2

    def transformed_rating(self,player):
        '''
        Returns the transformed score of a player.

        Transformed score is caluclated thusly:

        R = player's current elo rating

        Transformed score = 10^(R/400)
        '''
        return math.pow(10,player.elo/400)

    def expected_score(self,player1,player2):
        '''
        Returns a list of percent chance that each player
        is expected to win.

        Expected scores are calcuated thusly. 

        Q_1 := transformed rating for player 1
        Q_1 := transformed rating for player 1

        E_1 = Q_1/(Q_1+Q_2)
        E_2 = Q_2/(Q_1+Q_2)

        returns Q_1,Q_2
        '''
        p1_transform = self.transformed_rating(player1)
        p2_transform = self.transformed_rating(player2)

        p1_expected = p1_transform/(p1_transform+p2_transform)
        p2_expected = p2_transform/(p1_transform+p2_transform)

        return p1_expected,p2_expected

    def update_elo(self,player1,player2,score):

        '''
        Calucates and updates the elo for two players
        after a match has been performed.

        player1 and player2 are player objects
        score is an iterable contianing the score of the match
            
            (1,0) indicates a win for player1
            (0,1) indicates a win for player2
            (.5,.5) indicates a draw

        ELO updates are calculates thusly:

        p1_elo = current elo for player 1
        p2_elo = current elo for player 2

        E_1 = expected score for player 1
        E_2 = expected score for player 2

        k = k factor for the ELO System

        updated_p1_score = p1_elo + k*(p1_score - E_1)
        updated_p2_score = p2_elo + k*(p2_score - E_2)
        '''
        score = tuple(score)
        
        p1_expected,p2_expected = self.expected_score(player1,player2)
        p1_score = score[0]
        p2_score = score[1]

        player1.elo += self.factor*(p1_score-p1_expected)
        player2.elo += self.factor*(p2_score-p2_expected)

        if score == (1,0):
            player1.wins += 1
            player2.losses += 1
        elif score == (0,1):
            player1.losses += 1
            player2.wins += 1
        elif score == (.5,.5):
            player1.draws += 1
            player2.draws += 1
        else:
            print "Not a valid match score"

    def __str__(self):
        return "ELO System with k-factor %d" % self.factor

    __repr__ = __str__