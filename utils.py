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
        myPlay = 2
        oponentPlay = 0

        while not endOfInput:
            value = input()
            currentPlay = []
            if value == self.END_OF_INPUT:
                endOfInput = True
            else:
                currentPlay.append(value[oponentPlay])
                currentPlay.append(value[myPlay])
                myInput.append(currentPlay)
        return myInput
