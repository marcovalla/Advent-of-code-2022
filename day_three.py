class DayThree:

    def getSumOfPriorities(self, myInput):
        sumOfPriorities = 0
        for value in myInput:
            repeatedItems = self.getRepeatedItems(value)
            priority = 0
            for item in repeatedItems:
                priority += self.getItemPriority(item)
            sumOfPriorities += priority
        return sumOfPriorities

    def getSumOfPrioritiesForThreeElves(self, myInput):
        myInput = self.processInput(myInput)
        sumOfPriorities = 0
        for value in myInput:
            repeatedItems = self.getRepeatedItemsInThreeRucksacks(value)
            priority = 0
            for item in repeatedItems:
                priority += self.getItemPriority(item)
            sumOfPriorities += priority
        return sumOfPriorities

    def processInput(self, input):
        myInput = []
        for i in range(0, len(input), 3):
            groupOfThreeRucksacks = [input[i], input[i + 1], input[i + 2]]
            myInput.append(groupOfThreeRucksacks)
        return myInput

    def getRepeatedItemsInThreeRucksacks(self, collectionOfRucksacks):
        collectionOfRucksacks.sort(reverse=True)
        repeatedItems = []
        for i in range(len(collectionOfRucksacks[0])):
            currentItem = collectionOfRucksacks[0][i]
            if not repeatedItems.__contains__(currentItem):
                if collectionOfRucksacks[1].count(currentItem) > 0:
                    if collectionOfRucksacks[2].count(currentItem) > 0:
                        repeatedItems.append(currentItem)
        return repeatedItems

    def getRepeatedItems(self, rucksack):
        firstCompartment = []
        repeatedItems = []
        for i in range(len(rucksack)):
            if i < (len(rucksack) / 2):
                firstCompartment.append(rucksack[i])
            else:
                if firstCompartment.count(rucksack[i]) > 0 and not repeatedItems.__contains__(rucksack[i]):
                    repeatedItems.append(rucksack[i])
        return repeatedItems

    def getItemPriority(self, item):
        itemToASCII = ord(item)
        aLetterASCII = 97
        ALetterASCII = 65
        if item.islower():
            itemPriority = itemToASCII - aLetterASCII + 1
        elif item.isupper():
            itemPriority = itemToASCII - ALetterASCII + 27
        return itemPriority
