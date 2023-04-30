from Node import Node


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

    def insert(self, value):
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