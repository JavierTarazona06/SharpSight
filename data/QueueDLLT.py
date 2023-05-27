from data.DoubleLinkedListTail import *


class QueueDLLT(DoubleLinkedListTail):

    def __init__(self):
        super().__init__()

    def enqueue(self, newNode):
        self.pushFront(newNode)

    def dequeue(self):
        if not self.isEmpty():
            data = self.topBack()
            self.popBack()
            return data
        else:
            raise Exception("Queue is empty")

    def first(self):
        return self.topBack()

    def last(self):
        return self.topFront()