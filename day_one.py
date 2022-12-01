class DayOne:

    def getMaxAmountOfCalories(self, myInput):
        calories = self.__getCaloriesByElf(myInput)
        calories.sort(reverse = True)
        return calories[0]

    def getMaxAmountOfCaloriesForThreeElves(self, myInput):
        calories = self.__getCaloriesByElf(myInput)
        calories.sort(reverse = True)
        return calories[0]+calories[1]+calories[2]

    def __getCaloriesByElf(self, myInput):
        listOfTotalCalories = []
        currentAmountOfCalories = 0
        for value in myInput:
            if value != '':
                currentAmountOfCalories = currentAmountOfCalories + int(value)
            else:
                listOfTotalCalories.append(currentAmountOfCalories)
                currentAmountOfCalories = 0
        return listOfTotalCalories
