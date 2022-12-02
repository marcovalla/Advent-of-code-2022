class DayTwo:
    ROCK = "R"
    PAPER = "P"
    SCISSORS = "S"
    ROCK_SCORE = 1
    PAPER_SCORE = 2
    SCISSORS_SCORE = 3
    WIN_SCORE = 6
    DRAW_SCORE = 3
    LOSE_SCORE = 0
    LOSE = "L"
    DRAW = "D"
    WIN = "W"

    def getTotalScorePartOne(self, myInput):
        totalScore = 0
        for values in myInput:
            myHand = self.getHand(values[1])
            oponentsHand = self.getHand(values[0])
            totalScore += self.getRoundResultScore(myHand, oponentsHand) + self.getHandScore(myHand)
        return totalScore

    def getTotalScorePartTwo(self, myInput):
        totalScore = 0
        for values in myInput:
            plannedResult = self.getPlannedResult(values[1])
            oponentsHand = self.getHand(values[0])
            myHand = self.getPlannedHand(plannedResult, oponentsHand)
            totalScore += self.getRoundResultScore(myHand, oponentsHand) + self.getHandScore(myHand)
        return totalScore

    def getRoundResultScore(self, playerOne, playerTwo):
        if playerOne == playerTwo:
            return self.DRAW_SCORE
        else:
            if self.playerWin(playerOne, playerTwo):
                return self.WIN_SCORE
            else:
                return self.LOSE_SCORE

    def playerWin(self, playerOne, playerTwo):
        return (playerOne == self.ROCK and playerTwo == self.SCISSORS) or (playerOne == self.PAPER and playerTwo == self.ROCK) or (playerOne == self.SCISSORS and playerTwo == self.PAPER)

    def getHandScore(self, playersHand):
        if playersHand == self.ROCK:
            return self.ROCK_SCORE
        elif playersHand == self.PAPER:
            return self.PAPER_SCORE
        elif playersHand == self.SCISSORS:
            return self.SCISSORS_SCORE

    def getHand(self, value):
        if value == "X" or value == "A":
            return self.ROCK
        elif value == "Y" or value == "B":
            return self.PAPER
        elif value == "Z" or value == "C":
            return self.SCISSORS

    def getPlannedResult(self, value):
        if value == "X":
            return self.LOSE
        elif value == "Y":
            return self.DRAW
        elif value == "Z":
            return self.WIN

    def getPlannedHand(self, plannedResult, oponentsHand):
        if plannedResult == self.DRAW:
            return oponentsHand
        elif plannedResult == self.WIN:
            return self.getWinningHand(oponentsHand)
        elif plannedResult == self.LOSE:
            return self.getWinningHand(self.getWinningHand(oponentsHand))

    def getWinningHand(self, oponentsHand):
        if oponentsHand == self.ROCK:
            return self.PAPER
        elif oponentsHand == self.PAPER:
            return self.SCISSORS
        elif oponentsHand == self.SCISSORS:
            return self.ROCK
