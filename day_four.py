class DayFour:

    def getAmountOfContainedRanges(self, input):
        myInput = self.processInput(input)
        count = 0
        for team in myInput:
            firstElf = team[0]
            secondElf = team[1]
            if self.isOverlapped(firstElf, secondElf) or self.isOverlapped(secondElf, firstElf):
                count += 1
        return count

    def getAmountOfOverlappingRanges(self, input):
        myInput = self.processInput(input)
        count = 0
        for team in myInput:
            firstElf = team[0]
            secondElf = team[1]
            if self.isOverlappedAtAll(firstElf, secondElf) or self.isOverlappedAtAll(secondElf, firstElf):
                count += 1
        return count


    def isOverlapped(self, range1, range2):
        firstElfStart = int(range1.split("-")[0])
        firstElfEnd = int(range1.split("-")[1])
        secondElfStart = int(range2.split("-")[0])
        secondElfEnd = int(range2.split("-")[1])
        overlapped = False
        if firstElfStart >= secondElfStart and firstElfEnd <= secondElfEnd:
            overlapped = True
        return overlapped

    def isOverlappedAtAll(self, range1, range2):
        firstElfStart = int(range1.split("-")[0])
        firstElfEnd = int(range1.split("-")[1])
        secondElfStart = int(range2.split("-")[0])
        secondElfEnd = int(range2.split("-")[1])
        overlapped = False
        if firstElfStart <= secondElfEnd and firstElfEnd >= secondElfStart:
            overlapped = True
        return overlapped

    def processInput(self, input):
        myInput = []
        for value in input:
            splitByElf = value.split(",")
            myInput.append(splitByElf)
        return myInput
