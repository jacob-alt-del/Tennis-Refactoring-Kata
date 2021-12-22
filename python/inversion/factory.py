from abc  import ABC, abstractmethod

class Score(ABC):

    @abstractmethod
    def return_score(self):
        pass


class Draw(Score):

    def return_score(self):
        result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
        return result

class AdvantagePlayer(Score):

    def return_score(self):
        minusResult = self.p1points-self.p2points
        if (minusResult==1):
            result ="Advantage " + self.player1Name
        elif (minusResult ==-1):
            result ="Advantage " + self.player2Name
        elif (minusResult>=2):
            result = "Win for " + self.player1Name
        else:
            result ="Win for " + self.player2Name
        return result

class PointsPlayer(Score):

    def return_score(self, result):
        for i in range(1,3):
            if (i==1):
                tempScore = self.p1points
            else:
                result+="-"
                tempScore = self.p2points
            result += {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty",
            }[tempScore]
        return result
