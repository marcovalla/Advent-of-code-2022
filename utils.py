class Utils:

    END_OF_INPUT = '.'

    def getInputDayOne(self):
        myInput = []
        endOfInput = False

        while not endOfInput:
            value = input()
            if value == self.END_OF_INPUT:
                myInput.append('')
                endOfInput = True
            else:
                myInput.append(value)
        return myInput

    def getInputDayTwo(self):
        myInput = []
        endOfInput = False
        firstValue = 0
        secondValue = 2

        while not endOfInput:
            value = input()
            currentPlay = []
            if value == self.END_OF_INPUT:
                endOfInput = True
            else:
                currentPlay.append(value[firstValue])
                currentPlay.append(value[secondValue])
                myInput.append(currentPlay)
        return myInput
