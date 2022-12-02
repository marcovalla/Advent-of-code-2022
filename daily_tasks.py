from day_one import DayOne
from day_two import DayTwo
from utils import Utils


class DailyTasks:

    utils = Utils()

    def runDayOne(self):
        dayOne = DayOne()

        print("Enter input ended by '.' : ")
        myInput = self.utils.getInputDayOne()

        partOne = dayOne.getMaxAmountOfCalories(myInput)
        print("The max amount of calories carried by a single elf: ", partOne)

        partTwo = dayOne.getMaxAmountOfCaloriesForThreeElves(myInput)
        print("The max amount of calories carried by the top three elves: ", partTwo)

    def runDayTwo(self):
        dayTwo = DayTwo()

        print("Enter input ended by '.' : ")
        myInput = self.utils.getInputDayTwo()

        partOne = dayTwo.getTotalScorePartOne(myInput)
        print("The total score following the first strategy is: ", partOne)

        partTwo = dayTwo.getTotalScorePartTwo(myInput)
        print("The total score following the second strategy is: ", partTwo)
