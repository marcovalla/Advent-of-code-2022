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

    def getTotalScorePartOne(self, input):
        myInput = self.processInput(input)
        totalScore = 0
        for values in myInput:
            myHand = self.getHand(values[1])
            opponentsHand = self.getHand(values[0])
            totalScore += self.getRoundResultScore(myHand, opponentsHand) + self.getHandScore(myHand)
        return totalScore

    def processInput(self, input):
        myInput = []
        firstValue = 0
        secondValue = 2
        for i in range(len(input)):
            value = input[i]
            currentPlay = [value[firstValue], value[secondValue]]
            myInput.append(currentPlay)
        return myInput

    def getTotalScorePartTwo(self, myInput):
        totalScore = 0
        for values in myInput:
            plannedResult = self.getPlannedResult(values[1])
            opponentsHand = self.getHand(values[0])
            myHand = self.getPlannedHand(plannedResult, opponentsHand)
            totalScore += self.getRoundResultScore(myHand, opponentsHand) + self.getHandScore(myHand)
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
        rockBeatsScissors = playerOne == self.ROCK and playerTwo == self.SCISSORS
        paperBeatsRock = playerOne == self.PAPER and playerTwo == self.ROCK
        scissorsBeatsPaper = playerOne == self.SCISSORS and playerTwo == self.PAPER
        winCondition = rockBeatsScissors or paperBeatsRock or scissorsBeatsPaper
        return winCondition

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

    def getPlannedHand(self, plannedResult, opponentsHand):
        if plannedResult == self.DRAW:
            return opponentsHand
        elif plannedResult == self.WIN:
            return self.getWinningHand(opponentsHand)
        elif plannedResult == self.LOSE:
            return self.getWinningHand(self.getWinningHand(opponentsHand))

    def getWinningHand(self, opponentsHand):
        if opponentsHand == self.ROCK:
            return self.PAPER
        elif opponentsHand == self.PAPER:
            return self.SCISSORS
        elif opponentsHand == self.SCISSORS:
            return self.ROCK
