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

    def find(self, node_To_Find):
        return not self.findPosition(node_To_Find)==-1

    def findPosition(self, node_To_Find):
        if not self.isEmpty():
            ptr = self.head
            i=0
            while (not ptr is None):
                if ptr.key==node_To_Find.key:
                    return i
                ptr = ptr.next
                i+=1
            return -1
        else:
            raise Exception("List is empty")

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


    def insertOrder(self, new_node):
        if self.isEmpty() or new_node.key < self.head.key:
            new_node.next = self.head
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.key < new_node.key:
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node

    def delete(self, node_bye):
        if self.isEmpty():
            raise Exception("Empty List")
        elif self.head.key == node_bye.key:
            self.head = self.head.next
        else:
            curr_node = self.head
            prev_node = None
            while curr_node and curr_node.key != node_bye.key:
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node:
                prev_node.next = curr_node.next

    def sort(self):
        if not self.isEmpty():
            linkedListSorted = LinkedList()
            ptr_Or = self.head
            while not (ptr_Or is None):
                ptr_nw = Node(ptr_Or.key)
                linkedListSorted.insertOrder(ptr_nw)
                ptr_Or = ptr_Or.next
            self.head = linkedListSorted.head

    def reverse(self):
        if not self.isEmpty():
            linkedListReversed = LinkedList()
            ptr_Or = self.head
            while not (ptr_Or is None):
                linkedListReversed.pushFront(Node(ptr_Or.key))
                ptr_Or = ptr_Or.next
            self.head = linkedListReversed.head

    def reversedSort(self):
        self.sort()
        self.reverse()