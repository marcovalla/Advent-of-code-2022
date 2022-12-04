from day_four import DayFour
from day_one import DayOne
from day_three import DayThree
from day_two import DayTwo
from utils import Utils


class DailyTasks:

    utils = Utils()
    DAILY_TASKS_PATH = "Daily inputs/"

    def runDayOne(self):
        dayOne = DayOne()
        dayOnePath = self.DAILY_TASKS_PATH + "Day one.txt"
        myInput = self.utils.getInputFromFile(dayOnePath)
        partOne = dayOne.getMaxAmountOfCalories(myInput)
        print("The max amount of calories carried by a single elf: ", partOne)

        partTwo = dayOne.getMaxAmountOfCaloriesForThreeElves(myInput)
        print("The max amount of calories carried by the top three elves: ", partTwo)

    def runDayTwo(self):
        dayTwo = DayTwo()
        dayTwoPath = self.DAILY_TASKS_PATH + "Day two.txt"
        myInput = self.utils.getInputFromFile(dayTwoPath)

        partOne = dayTwo.getTotalScorePartOne(myInput)
        print("The total score following the first strategy is: ", partOne)

        partTwo = dayTwo.getTotalScorePartTwo(myInput)
        print("The total score following the second strategy is: ", partTwo)

    def runDayThree(self):
        dayThree = DayThree()
        dayThreePath = self.DAILY_TASKS_PATH + "Day three.txt"
        myInput = self.utils.getInputFromFile(dayThreePath)

        partOne = dayThree.getSumOfPriorities(myInput)
        print("The total sum of the priorities is: ", partOne)

        partTwo = dayThree.getSumOfPrioritiesForThreeElves(myInput)
        print("The total sum of the priorities for three elves is: ", partTwo)

    def runDayFour(self):
        dayFour = DayFour()
        dayFourPath = self.DAILY_TASKS_PATH + "Day four.txt"
        myInput = self.utils.getInputFromFile(dayFourPath)

        partOne = dayFour.getAmountOfContainedRanges(myInput)
        print("The amount of teams with contained ranges is: ", partOne)

        partTwo = dayFour.getAmountOfOverlappingRanges(myInput)
        print("The amount of teams with overlapped ranges is: ", partTwo)
