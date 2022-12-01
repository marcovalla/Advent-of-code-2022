class Utils:

    def getInput(self):
        myInput = []
        endOfInput = False

        while not endOfInput:
            value = input()
            if value == '.':
                myInput.append('')
                endOfInput = True
            else:
                myInput.append(value)
        return myInput
