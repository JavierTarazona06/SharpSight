from data.DoubleLinkedListTail import *


class Stack(DoubleLinkedListTail):

    def __init__(self):
        super().__init__()

    def push(self, newNode):
        self.pushFront(newNode)

    def pop(self):
        if not self.isEmpty():
            data = self.topFront()
            self.popFront()
            return data
        else:
            raise Exception("Stack is empty")

    def peek(self):
        return self.topFront()
