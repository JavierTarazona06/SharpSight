import math

from data.DynamicList import DynamicList


class Heap:

    def __init__(self):
        self.array = DynamicList()

    def getSize(self):
        return self.array.index

    def getMaxSize(self):
        return self.array.size

    def parent(self, index):
        indexParent = ((index + 1) // 2) - 1
        if indexParent >= self.getSize():
            raise Exception(
                "No parent: Index " + str(indexParent) + " out of bounds for size " + str(self.getSize()))
        else:
            return indexParent

    def leftChild(self, index):
        indexChildL = ((index + 1) * 2) - 1
        if indexChildL >= self.getSize():
            raise Exception(
                "No left child: Index " + str(indexChildL) + " out of bounds for size " + str(self.getSize()))
        else:
            return indexChildL

    def rightChild(self, index):
        indexChildR = (((index + 1) * 2) + 1) - 1
        if indexChildR >= self.getSize():
            raise Exception(
                "No right child: Index " + str(indexChildR) + " out of bounds for size " + str(self.getSize()))
        else:
            return indexChildR

    def levelNode(self, index):
        i = index + 1
        return int((math.log(i) / math.log(2)) + 1)

    def insert(self, key):
        self.array.pushBack(key)

    def lineToInsert(self, data):
        dataList = data.split(" ")
        for s in dataList:
            self.insert(int(s))

    def levelOrder(self):
        if self.array.empty():
            raise Exception("Empty Heap")
        else:
            l = 1
            result = ""
            for i in range(self.getSize()):
                cur_element = self.array.list[i]
                cur_level = self.levelNode(i)
                if (l + 1) == cur_level:
                    result += "\n" + str(cur_element) + " "
                    l += 1
                else:
                    result += str(cur_element) + " "
            return result

    def inOrderCall(self, index):
        if index == self.getSize():
            return ""
        else:
            result = ""
            try:
                result += self.inOrderCall(self.leftChild(index))
            except Exception:
                pass
            num = self.array.list[index]
            result += str(num) + " "
            try:
                result += self.inOrderCall(self.rightChild(index))
            except Exception:
                pass
            return result

    def inOrder(self):
        return self.inOrderCall(0)

    def preOrderCall(self, index):
        if index == self.getSize():
            return ""
        else:
            result = ""
            num = self.array.list[index]
            result += str(num) + " "
            try:
                result += self.preOrderCall(self.leftChild(index))
            except Exception:
                pass
            try:
                result += self.preOrderCall(self.rightChild(index))
            except Exception:
                pass
            return result

    def preOrder(self):
        return self.preOrderCall(0)

    def posOrderCall(self, index):
        if index == self.getSize():
            return ""
        else:
            result = ""
            try:
                result += self.posOrderCall(self.leftChild(index))
            except Exception:
                pass
            try:
                result += self.posOrderCall(self.rightChild(index))
            except Exception:
                pass
            num = self.array.list[index]
            result += str(num) + " "
            return result

    def posOrder(self):
        return self.posOrderCall(0)

    def remove(self, index):
        if index == (self.getSize() - 1):
            self.array.index -= 1
        elif index < (self.getSize() - 1):
            self.array.list[index] = self.array.list[index + 1]
            self.remove(index + 1)
        else:
            raise Exception("Index " + str(index) + " out of bounds for size: " + str(self.getSize()))

    def changePriority(self, index, new_Value):
        self.array.list[index] = new_Value
