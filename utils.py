class Utils:

    END_OF_INPUT = '.'

    def getInput(self):
        myInput = []
        endOfInput = False

        while not endOfInput:
            value = input()
            if value == self.END_OF_INPUT:
                endOfInput = True
            else:
                myInput.append(value)
        return myInput
