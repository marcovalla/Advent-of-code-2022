class Node:

    def __init__(self, nodeName: str, nodeWeight: int, father):
        self.name = nodeName
        self.weight = nodeWeight
        self.father = father
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getFather(self):
        return self.father

    def getChildren(self):
        return self.children

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getChild(self, child):
        for c in self.children:
            if c.getName() == child:
                return c

    def toString(self):
        print("node name: ",self.name, " children: ", self.children)
        for c in self.children:
            c.toString()
