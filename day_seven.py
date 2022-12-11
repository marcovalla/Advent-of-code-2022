from Node import Node


class DaySeven:

    def getSumOfSizesOfSelectedDirectories(self, myInput):
        rootNode = self.getDirectory(myInput)

        sumOfSizes = 0

        return sumOfSizes

    def getDirectory(self, input):
        lineIndex = 0
        rootNode = Node("/", -1, None)
        currentDir = rootNode
        for i in range(len(input)):
            line = input[lineIndex]
            print(line)
            if line == "$ ls":
                lineIndex = self.setCurrentDirectory(input, lineIndex, currentDir)
            elif line[:4] == "$ cd":
                if line[4:] == "..":
                    currentDir = currentDir.getFather()
                else:
                    child = line[4:]
                    currentDir = currentDir.getChild(child)
            lineIndex += 1
        return rootNode

    def setCurrentDirectory(self, input, lineIndex, currentDir: Node):
        
        endOfList = False
        while not endOfList:
            lineIndex += 1
            line = input[lineIndex]
            if line[0] == "$":
                endOfList = True
            else:
                lineElements = line.split(" ")
                if lineElements[0] == "dir":
                    newDirChild = Node(lineElements[1], -1, currentDir)
                    currentDir.addChild(newDirChild)
                else:
                    newFileChild = Node(lineElements[0], int(lineElements[1]), currentDir)
                    currentDir.addChild(newFileChild)
        return lineIndex
