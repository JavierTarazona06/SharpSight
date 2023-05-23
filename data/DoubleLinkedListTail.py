from data.LinkedList import LinkedList
from data.Node import Node


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
            if self.head.next is None:
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

    def insert(self,index,newNode):
        if index==0:
            self.pushFront(newNode)
        else:
            ptr = self.head
            acc = 0
            while acc<index-1:
                ptr = ptr.next
                acc+=1
            if not ptr:
                raise ValueError("Position out of range")
            newNode.next = ptr.next
            ptr.next = newNode
            newNode.prev = ptr
            if (newNode.next is not None):
                newNode.next.prev = newNode
            else:
                self.tail = newNode

    def insertOrder(self, new_node):
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        elif new_node.key < self.head.key:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.key < new_node.key:
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.tail = new_node

    def insertOrderPrice(self, new_node):
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        elif new_node.key.price < self.head.key.price:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.key.price < new_node.key.price:
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.tail = new_node

    def sort(self):
        if not self.isEmpty():
            linkedListSorted = DoubleLinkedListTail()
            ptr_Or = self.head
            while not (ptr_Or is None):
                ptr_nw = Node(ptr_Or.key)
                linkedListSorted.insertOrder(ptr_nw)
                ptr_Or = ptr_Or.next
            self.head = linkedListSorted.head
            self.tail = linkedListSorted.tail

    def sortPrice(self):
        if not self.isEmpty():
            linkedListSorted = DoubleLinkedListTail()
            ptr_Or = self.head
            while not (ptr_Or is None):
                ptr_nw = Node(ptr_Or.key)
                linkedListSorted.insertOrderPrice(ptr_nw)
                ptr_Or = ptr_Or.next
            self.head = linkedListSorted.head
            self.tail = linkedListSorted.tail

    def filterPriceGreater(self,priceFiltered):
        if not self.isEmpty():
            linkedListFiltered = DoubleLinkedListTail()
            ptr_Or = self.head
            while not (ptr_Or is None):
                ptr_nw = Node(ptr_Or.key)
                if (ptr_nw.key.price>=priceFiltered):
                    linkedListFiltered.insertOrderPrice(ptr_nw)
                ptr_Or = ptr_Or.next
            self.head = linkedListFiltered.head
            self.tail = linkedListFiltered.tail

    def filterPriceLower(self,priceFiltered):
        if not self.isEmpty():
            linkedListFiltered = DoubleLinkedListTail()
            ptr_Or = self.head
            while not (ptr_Or is None):
                ptr_nw = Node(ptr_Or.key)
                if (ptr_nw.key.price<=priceFiltered):
                    linkedListFiltered.insertOrderPrice(ptr_nw)
                ptr_Or = ptr_Or.next
            self.head = linkedListFiltered.head
            self.tail = linkedListFiltered.tail

    def reverse(self):
        if not self.isEmpty():
            linkedListReversed = DoubleLinkedListTail()
            ptr_Or = self.head
            while not (ptr_Or is None):
                linkedListReversed.pushFront(Node(ptr_Or.key))
                ptr_Or = ptr_Or.next
            self.head = linkedListReversed.head
            self.tail = linkedListReversed.tail

    def strProductList(self):
        if self.isEmpty():
            return ""
        else:
            list = []
            headRef = self.head
            while headRef.next is not None:
                prod = headRef.key
                list.append(str(prod)+"\n")
                headRef = headRef.next
            prod = headRef.key
            list.append(str(prod))
            return "".join(list)