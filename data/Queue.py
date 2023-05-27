from data.DoubleLinkedListTail import DoubleLinkedListTail

class Queue(DoubleLinkedListTail):

    def __init__(self):
        super().__init__()

    def enqueue(self, newNode):
        self.pushBack(newNode)

    def dequeue(self):
        if not self.isEmpty():
            data = self.topFront()
            self.popFront()
            return data
        else:
            raise Exception("Queue is empty")

    def first(self):
        return self.topFront()