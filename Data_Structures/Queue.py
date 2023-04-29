from LinkedList import LinkedList

class Queue(LinkedList):

    def __init__(self):
        super().__init__()

    def enqueue(self, newNode):
        self.pushBack(newNode)

    def dequeue(self):
        data = self.topFront()
        self.popFront()
        return data