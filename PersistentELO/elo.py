import math
import player

class ELO(object):
    
    """Creates an ELO object.

    Arguments:

    k_factor (int) - the k-factor to use in calculations

    Usage:

    >>>e = ELO()

    or

    >>>e = ELO(k_factor=25) #for an elo with k-factor of 25

    """
    
    def __init__(self,k_factor=32):
        self.k_factor = k_factor

    def expected_victor(self,p1,p2):
        
        """Returns the player with the higher elo
        as that player is expected to win.

        Arguments:

        p1 (player object) - the first player to compare
        p2 (player object) - the second player to compare

        Note:

        In the event of both players having the same elo,
        it returns the first parameter player.

        """
        
        return p1 if p1 >= p2 else p2

    def transformed_rating(self,p):
        
        """Returns the transformed score of a player.

        Arguments:

        p (player object) - player to calculate transformed rating of



        Transformed score is caluclated thusly:

        R = player's current elo rating

        Transformed score = 10^(R/400)

        """

        return math.pow(10,p.rating/400)

    def expected_score(self,p1,p2):

        """Returns a list of percent chance that each player
        is expected to win.

        Expected scores are calcuated thusly: 

        Q_1 := transformed rating for player 1
        Q_2 := transformed rating for player 2

        E_1 := expected score for player 1
        E_2 := expected score for player 1

        E_1 = Q_1/(Q_1+Q_2)
        E_2 = Q_2/(Q_1+Q_2)

        returns E_1,E_2
        
        """

        p1_transform = self.transformed_rating(p1)
        p2_transform = self.transformed_rating(p2)

        p1_expected = p1_transform/(p1_transform+p2_transform)
        p2_expected = p2_transform/(p1_transform+p2_transform)

        return p1_expected,p2_expected

    def update_elo(self,p1,p2,score):
        
        """Calucates and updates the elo for two players
        after a match has been performed.

        player1 and player2 are player objects
        score is an iterable contianing the score of the match
            
            (1,0) indicates a win for player 1
            (0,1) indicates a win for player 2
            (.5,.5) indicates a draw

        ELO updates are calculates thusly:

        p1_elo = current elo for player 1
        p2_elo = current elo for player 2

        E_1 = expected score for player 1
        E_2 = expected score for player 2

        k = k factor for the ELO System

        updated_p1_score = p1_elo + k*(p1_score - E_1)
        updated_p2_score = p2_elo + k*(p2_score - E_2)

        Note:

        If p1 and p2 are the same object this will print an error
        
        """

        if p1 is not p2:

            score = tuple(score)
            
            p1_expected,p2_expected = self.expected_score(p1,p2)

            p1_score = score[0]
            p2_score = score[1]

            p1.rating += self.k_factor*(p1_score-p1_expected)
            p2.rating += self.k_factor*(p2_score-p2_expected)

            if score == (1,0):
                p1.wins += 1
                p2.losses += 1
            elif score == (0,1):
                p1.losses += 1
                p2.wins += 1
            elif score == (.5,.5):
                p1.draws += 1
                p2.draws += 1
            else:
                print("Not a valid match score")

    def __str__(self):

        """Prints the k-factor of the ELO system"""

        return "ELO System with k-factor %d" % self.k_factor

    __repr__ = __str__