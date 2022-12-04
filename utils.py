class Utils:

    END_OF_INPUT = '.'

    def getInputFromConsole(self):
        print("Enter input ended by '.'")
        myInput = []
        endOfInput = False

        while not endOfInput:
            value = input()
            if value == self.END_OF_INPUT:
                endOfInput = True
            else:
                myInput.append(value)
        return myInput

    def getInputFromFile(self, filepath):
        file = open(filepath, "r")
        myInput = []
        for line in file:
            myInput.append(line.replace("\n", ""))
        file.close()
        return myInput
