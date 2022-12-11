class DaySix:

    SIZE_OF_PACKET_MARKER = 4
    SIZE_OF_MESSAGE_MARKER = 14

    def getFirstStartOfPacketMarkerIndex(self, input):
        return self.getSetOfUniqueCharsForSize(input, self.SIZE_OF_PACKET_MARKER)

    def getFirstStartOfPacketMessageIndex(self, input):
        return self.getSetOfUniqueCharsForSize(input, self.SIZE_OF_MESSAGE_MARKER)

    def processInput(self, input):
        myInput = ""
        for line in input:
            myInput += line
        return myInput

    def getSetOfUniqueCharsForSize(self, input, size):
        myInput = self.processInput(input)
        charIndex = 0
        markerFounded = False
        while not markerFounded and (charIndex + size) <= len(myInput):
            listOfChar = []
            index = charIndex
            for i in range(size):
                listOfChar.append(myInput[index])
                index += 1
            setOfChars = set(listOfChar)
            if len(setOfChars) == size:
                markerFounded = True
            else:
                charIndex += 1
        return charIndex + size
