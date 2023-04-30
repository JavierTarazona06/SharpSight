from typing import TypeVar, Generic

from Node import Node

T = TypeVar('T')

class LinkedList(Generic[T]):
    # Constr.
    def __init__(self):
        self.head = None

    # Meth.
    def pushFront(self, newNode):
        newNode.next = self.head
        self.head = newNode

    def popFront(self):
        if not self.isEmpty():
            self.head = self.head.next
        else:
            raise Exception("Fail popFront. Linked List Vacia")

    def topFront(self):
        data = None
        if not self.isEmpty():
            data = self.head.key
        else:
            raise Exception("Fail topFront. Linked List Vacia")
        return data

    def pushBack(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            headRef = self.head
            while headRef.next != None:
                headRef = headRef.next
            headRef.next = newNode

    def popBack(self):
        if not self.isEmpty():
            if self.head.next == None:
                self.head = None
            else:
                headRef = self.head
                while headRef.next.next != None:
                    headRef = headRef.next
                headRef.next = None
        else:
            raise Exception("Fail popBack. Linked List Vacia")

    def topBack(self):
        ans = None
        if not self.isEmpty():
            headRef = self.head
            while headRef.next != None:
                headRef = headRef.next
            ans = headRef.key
        else:
            raise Exception("Fail topBack. Linked List Vacia")
        return ans

    def print(self):
        headRef = self.head
        while headRef != None:
            print(headRef.key, end=" ")
            headRef = headRef.next
        print("")

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            list = []
            headRef = self.head
            while headRef.next != None:
                list.append(str(headRef.key))
                headRef = headRef.next
            list.append(str(headRef.key))
            return " ".join(list)

    def printRecursive(self, headRef):
        if headRef != None:
            print(headRef.key, end=" ")
            self.printRecursive(headRef.next)
        else:
            print("")

    def isEmpty(self):
        return self.head == None

    def find(self, keyFind):
        flag = False
        return flag

    def size(self):
        headRef = self.head
        size = 0
        if self.isEmpty():
            return size
        else:
            while headRef.next != None:
                size += 1
                headRef = headRef.next
            return size + 1

    def insert(self,index,value):
        newNode = Node(value)
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


    def insertOrder(self, value):
        new_node = Node(value)
        if self.isEmpty() or value < self.head.key:
            new_node.next = self.head
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.key < value:
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node

    def delete(self, data):
        if self.isEmpty():
            raise Exception("Empty List")
        elif self.head.key == data:
            self.head = self.head.next
        else:
            curr_node = self.head
            prev_node = None
            while curr_node and curr_node.key != data:
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node:
                prev_node.next = curr_node.next