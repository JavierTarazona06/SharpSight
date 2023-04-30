from LinkedList import LinkedList

class DoubleLinkedListTail(LinkedList):

    def __init__(self):
        super().__init__()
        self.tail = None

    def pushFront(self, newNode):
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def popFront(self):
        if not self.isEmpty():
            if self.size() == 1:
                self.head = self.head.next
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            raise ValueError("Fail popFront. Linked List Vacia")

    def pushBack(self, newNode):
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def popBack(self):
        if not self.isEmpty():
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            raise ValueError("Fail popBack. Linked List Vacia")

    def topBack(self):
        if not self.isEmpty():
            return self.tail.key
        else:
            raise ValueError("Fail topBack. Linked List Vacia")
