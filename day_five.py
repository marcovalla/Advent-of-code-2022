class DayFive:

    NUMBER_OF_ROWS = 9

    def getTopCratesFromCrateMover9000(self, myInput):
        crates = self.getCrates(myInput)
        instructions = self.getInstructions(myInput)
        for instruction in instructions:
            moveI = instruction[0]
            fromI = instruction[1] - 1
            toI = instruction[2] - 1
            for i in range(moveI):
                if len(crates[fromI]) > 0:
                    crates[toI].append(crates[fromI].pop())
        topCrates = ""
        for crateRow in crates:
            topCrates += crateRow.pop()
        return topCrates

    def getTopCratesFromCrateMover9001(self, myInput):
        crates = self.getCrates(myInput)
        instructions = self.getInstructions(myInput)
        for instruction in instructions:
            moveI = instruction[0]
            fromI = instruction[1] - 1
            toI = instruction[2] - 1
            crateHandler = []
            for i in range(moveI):
                if len(crates[fromI]) > 0:
                    crateHandler.insert(0, crates[fromI].pop())
            crates[toI].extend(crateHandler)
        topCrates = ""
        for crateRow in crates:
            if len(crateRow) > 0:
                topCrates += crateRow.pop()
        return topCrates

    def getCrates(self, input):
        crates = []
        endOfCrates = False
        rows = self.NUMBER_OF_ROWS
        for i in range(rows):
            crates.append([])
        crateIndex = 0
        crateIndexIncrement = 4
        lineNumber = 0
        while not endOfCrates:
            charIndex = 1 + crateIndex * crateIndexIncrement
            crate = input[lineNumber][charIndex]
            if crate.isnumeric():
                endOfCrates = True
            else:
                if crate != " ":
                    crates[crateIndex].insert(0, crate)
                crateIndex += 1
                if crateIndex > rows - 1:
                    lineNumber += 1
                    crateIndex = 0
        return crates

    def getInstructions(self, input):
        instructions = []
        instructionsStarted = False
        for line in input:
            if not instructionsStarted:
                if line == "":
                    instructionsStarted = True
            else:
                currentLine = line.split(" ")
                moveI = int(currentLine[1])
                fromI = int(currentLine[3])
                toI = int(currentLine[5])
                instruction = [moveI, fromI, toI]
                instructions.append(instruction)
        return instructions
