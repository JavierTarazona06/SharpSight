from data.Node import Node


class LinkedListOrdered():
    # Constr.
    def __init__(self):
        self.head = None

    # Meth.
    def topFront(self):
        data = None
        if not self.isEmpty():
            data = self.head.key
        else:
            raise Exception("Fail topFront. Linked List Vacia")
        return data

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

    def getNode(self,index):
        if index>=self.size():
            raise Exception("Index out of bound")
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        return ptr

    def find(self,node_to_find):
        if self.isEmpty():
            raise Exception("Empty List")
        else:
            return not self.findPosition(node_to_find)==-1

    def findPosition(self, node_to_find):
        if self.isEmpty():
            raise Exception("Empty List")
        else:
            return self.binarySearch(0,self.size()-1,node_to_find)

    def binarySearch(self,inicio,fin,node_to_find):
        if fin>=inicio:
            mid = (fin+inicio)//2
            ptr = self.getNode(mid)
            if ptr.key == node_to_find.key:
                return mid
            elif ptr.key > node_to_find.key:
                return self.binarySearch(inicio,mid-1,node_to_find)
            else:
                return self.binarySearch(mid+1,fin,node_to_find)
        else:
            return -1

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

    def insert(self, new_node):
        if self.isEmpty() or ((new_node.key < self.head.key) and (not new_node.key == self.head.key)):
            new_node.next = self.head
            self.head = new_node
        else:
            ptr = self.head
            while (ptr.next is not None) and (ptr.next.key < new_node.key):
                ptr = ptr.next
            if ptr.next is None:
                if not ptr.key == new_node.key:
                    new_node.next = ptr.next
                    ptr.next = new_node
            elif not ptr.key == new_node.key:
                if not ptr.next.key == new_node.key:
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