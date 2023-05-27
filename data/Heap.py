import math

from data.DynamicList import DynamicList


class Heap:

    def __init__(self):
        self.array = DynamicList()

    def get_size(self):
        return self.array.index

    def get_max_size(self):
        return self.array.size

    def parent(self, index):
        indexParent = ((index + 1) // 2) - 1
        if indexParent >= self.get_size():
            raise Exception(
                "No parent: Index " + str(indexParent) + " out of bounds for size " + str(self.get_size()))
        else:
            return indexParent

    def left_child(self, index):
        indexChildL = ((index + 1) * 2) - 1
        if indexChildL >= self.get_size():
            raise Exception(
                "No left child: Index " + str(indexChildL) + " out of bounds for size " + str(self.get_size()))
        else:
            return indexChildL

    def right_child(self, index):
        indexChildR = (((index + 1) * 2) + 1) - 1
        if indexChildR >= self.get_size():
            raise Exception(
                "No right child: Index " + str(indexChildR) + " out of bounds for size " + str(self.get_size()))
        else:
            return indexChildR

    def level_node(self, index):
        i = index + 1
        return int((math.log(i) / math.log(2)) + 1)

    def insert(self, key):
        self.array.pushBack(key)

    def line_to_insert(self, data):
        dataList = data.split(" ")
        for s in dataList:
            self.insert(int(s))

    def level_order(self):
        if self.array.empty():
            raise Exception("Empty Heap")
        else:
            l = 1
            result = ""
            for i in range(self.get_size()):
                cur_element = self.array.list[i]
                cur_level = self.level_node(i)
                if (l + 1) == cur_level:
                    result += "\n" + str(cur_element) + " "
                    l += 1
                else:
                    result += str(cur_element) + " "
            return result

    def inOrderCall(self, index):
        if index == self.get_size():
            return ""
        else:
            result = ""
            try:
                result += self.inOrderCall(self.left_child(index))
            except Exception:
                pass
            num = self.array.list[index]
            result += str(num) + " "
            try:
                result += self.inOrderCall(self.right_child(index))
            except Exception:
                pass
            return result

    def in_order(self):
        return self.inOrderCall(0)

    def preOrderCall(self, index):
        if index == self.get_size():
            return ""
        else:
            result = ""
            num = self.array.list[index]
            result += str(num) + " "
            try:
                result += self.preOrderCall(self.left_child(index))
            except Exception:
                pass
            try:
                result += self.preOrderCall(self.right_child(index))
            except Exception:
                pass
            return result

    def pre_order(self):
        return self.preOrderCall(0)

    def posOrderCall(self, index):
        if index == self.get_size():
            return ""
        else:
            result = ""
            try:
                result += self.posOrderCall(self.left_child(index))
            except Exception:
                pass
            try:
                result += self.posOrderCall(self.right_child(index))
            except Exception:
                pass
            num = self.array.list[index]
            result += str(num) + " "
            return result

    def pos_order(self):
        return self.posOrderCall(0)

    def remove(self, index):
        if index == (self.get_size() - 1):
            self.array.index -= 1
        elif index < (self.get_size() - 1):
            self.array.list[index] = self.array.list[index + 1]
            self.remove(index + 1)
        else:
            raise Exception("Index " + str(index) + " out of bounds for size: " + str(self.get_size()))

    def change_priority(self, index, new_value):
        self.array.list[index] = new_value
