from typing import TypeVar, Generic

from data.Node import Node

T = TypeVar('T')

class LinkedList(Generic[T]):
    # Constr.
    def __init__(self):
        self.head:Node = None

    def __iter__(self) -> object:
        if self.isEmpty():
            raise Exception("Empty List")
        else:
            self.node_iterable:Node = self.head
            return self
    
    def __next__(self) -> object:
        if self.node_iterable is None:
            raise StopIteration
        else:
            cur_node:Node = self.node_iterable
            self.node_iterable = cur_node.next
            return cur_node.key

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            list = ["["]
            headRef:Node = self.head
            while headRef.next is not None:
                list.append(str(headRef.key)+", ")
                headRef = headRef.next
            list.append(str(headRef.key)+"]")
            return "".join(list)
        
    def print(self):
        headRef = self.head
        while headRef != None:
            print(headRef.key, end=" ")
            headRef = headRef.next
        print("")

    def printRecursive(self, headRef):
        if headRef != None:
            print(headRef.key, end=" ")
            self.printRecursive(headRef.next)
        else:
            print("")
        
    def to_list(self) -> list:
        if self.isEmpty():
            return []
        else:
            list = []
            headRef:Node = self.head
            while headRef.next is not None:
                list.append(headRef.key)
                headRef = headRef.next
            list.append(headRef.key)
            return list

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

    def isEmpty(self):
        return self.head is None

    def getNode(self,index):
        if index>=self.size():
            raise Exception("Index out of bound")
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        return ptr

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
            while headRef.next is not None:
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

    def delete(self, node_bye:Node):
        if self.isEmpty():
            raise Exception("Empty List")
        elif self.head.key == node_bye.key:
            self.head = self.head.next
        else:
            curr_node:Node = self.head
            prev_node = None
            while curr_node and curr_node.key != node_bye.key:
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node:
                prev_node.next = curr_node.next

    def replace(self, node_bye:Node, new_node:Node):
        if self.isEmpty():
            raise Exception("Empty List")
        elif self.head.key == node_bye.key:
            new_node.next = self.head.next
            self.head = new_node
        else:
            curr_node:Node = self.head
            prev_node = None
            while curr_node and curr_node.key != node_bye.key:
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node:
                prev_node.next = new_node
                new_node.next = curr_node.next

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