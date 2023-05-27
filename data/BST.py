from data.DynamicList import DynamicList
from data.Node import Node
from data.Stack import Stack
from data.NodeT import NodeT
from data.Queue import Queue


class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def size(self, ptr):
        if ptr is None:
            return 0
        else:
            return 1 + self.size(ptr.left) + self.size(ptr.right)

    def getSize(self):
        return self.size(self.root)

    def heightCall(self, ptr):
        if ptr is None:
            return 0
        else:
            l = self.heightCall(ptr.left)
            r = self.heightCall(ptr.right)
            return 1 + l if l > r else 1 + r

    def height(self):
        return self.heightCall(self.root)

    def levelCall(self, toSearch, ptr, checked):
        if ptr is None:
            if not checked:
                raise Exception("Node not in tree")
            else:
                return 0
        else:
            if toSearch == ptr.key:
                return 1
            elif toSearch > ptr.key:
                return 1 + self.levelCall(toSearch, ptr.right, checked)
            else:
                return 1 + self.levelCall(toSearch, ptr.left, checked)

    def level(self, toSearch):
        return self.levelCall(toSearch, self.root, False)

    def isNode(self, ptr):
        try:
            self.level(ptr.key)
            return True
        except Exception:
            return False

    def findCall(self, toSearch, ptr):
        if toSearch == ptr.key:
            return ptr
        elif toSearch > ptr.key:
            if ptr.right is not None:
                return self.findCall(toSearch, ptr.right)
            else:
                raise Exception("Node not in tree")
        else:
            if ptr.left is not None:
                return self.findCall(toSearch, ptr.left)
            else:
                raise Exception("Node not in tree")

    def find(self, toSearch):
        return self.findCall(toSearch, self.root)

    def prev(self, ptr):
        if ptr.left is not None:
            return self.rightDescendant(ptr.left)
        else:
            try:
                return self.leftAncestor(ptr)
            except Exception as e:
                return ptr.left

    def rightDescendant(self, ptr):
        return ptr if ptr.right is None else self.rightDescendant(ptr.right)

    def leftAncestorCall(self, fixed, ptr, stack):
        if ptr is not None:
            if fixed.key < ptr.key:
                return self.leftAncestorCall(fixed, ptr.left, stack)
            elif fixed.key > ptr.key:
                stack.push(Node(ptr))
                return self.leftAncestorCall(fixed, ptr.right, stack)
            else:
                return stack.pop()
        else:
            return None

    def leftAncestor(self, fixed):
        if self.isNode(fixed):
            stack = Stack()
            return self.leftAncestorCall(fixed, self.root, stack)
        else:
            raise Exception("Node not in tree")

    def next(self, ptr : NodeT) -> NodeT:
        if ptr.right is not None:
            return self.leftDescendant(ptr.right)
        else:
            try:
                return self.rightAncestor(ptr)
            except Exception as e:
                return ptr.right

    def leftDescendant(self, ptr):
        return ptr if ptr.left is None else self.leftDescendant(ptr.left)

    def rightAncestorCall(self, fixed, ptr, stack):
        if ptr is not None:
            if fixed.key < ptr.key:
                stack.push(Node(ptr))
                return self.rightAncestorCall(fixed, ptr.left, stack)
            elif fixed.key > ptr.key:
                return self.rightAncestorCall(fixed, ptr.right, stack)
            else:
                return stack.pop()
        else:
            return None

    def rightAncestor(self, fixed):
        if self.isNode(fixed):
            stack = Stack()
            return self.rightAncestorCall(fixed, self.root, stack)
        else:
            raise Exception("Node not in tree")

    def rangeSearch(self, x, y):
        values = DynamicList()
        st = self.find(x)
        while st is not None and (st.key < y or st.key == y):
            values.pushBack(int(st.key))
            st = self.next(st)
        return values

    def rangeSearchInvs(self, x, y):
        values = DynamicList()
        st = self.find(x)
        while st is not None and (st.key > y or st.key == y):
            values.pushBack(int(st.key))
            st = self.prev(st)
        return values

    def parentCall(self, son, ptr, poParent):
        if ptr is not None:
            if son.key < ptr.key:
                return self.parentCall(son, ptr.left, ptr)
            elif son.key > ptr.key:
                return self.parentCall(son, ptr.right, ptr)
            else:
                return poParent
        else:
            return ptr

    def parent(self, toSearch):
        if self.isNode(toSearch):
            return self.parentCall(toSearch, self.root, None)
        else:
            raise Exception("Node not in tree")

    def maxCall(self, ptr):
        if ptr.right is not None:
            return self.maxCall(ptr.right)
        else:
            return ptr

    def max(self):
        return self.maxCall(self.root)

    def minCall(self, ptr:NodeT) -> NodeT:
        if ptr.left is not None:
            return self.minCall(ptr.left)
        else:
            return ptr

    def min(self) -> NodeT:
        return self.minCall(self.root)

    def insertCall(self, num, ptr):
        if ptr is None:
            ptr = NodeT(num)
        else:
            if num < ptr.key:
                ptr.left = self.insertCall(num, ptr.left)
            else:
                if num > ptr.key:
                    ptr.right = self.insertCall(num, ptr.right)
                else:
                    print("El elemento ", num, " ya está en el árbol!")
        return ptr

    def insert(self, num):
        self.root = self.insertCall(num, self.root)

    def deleteCall(self, toDelete, ptr):
        if ptr is not None:
            if toDelete.key < ptr.key:
                ptr.left = self.deleteCall(toDelete, ptr.left)
            elif toDelete.key > ptr.key:
                ptr.right = self.deleteCall(toDelete, ptr.right)
            else:
                # Case of leaf or one child
                if ptr.left is None:
                    return ptr.right
                if ptr.right is None:
                    return ptr.left
                # Case with two children
                sig = self.next(ptr)
                ptr.key = sig.key
                ptr.right = self.deleteCall(sig, ptr.right)
            return ptr
        else:
            return None

    def delete(self, toDelete):
        if self.isNode(toDelete):
            self.root = self.deleteCall(toDelete, self.root)
        else:
            raise Exception("Node not in tree")

    def levelOrderCall(self, level, nlevel):
        if level.isEmpty():
            return ""
        else:
            cur_node = level.dequeue()

            if cur_node.left is not None:
                level.enqueue(Node(cur_node.left))
            if cur_node.right is not None:
                level.enqueue(Node(cur_node.right))

            if nlevel + 1 == self.level(cur_node.key):
                return "\n" + cur_node.key + " " + self.levelOrderCall(level, nlevel + 1)
            else:
                return cur_node.key + " " + self.levelOrderCall(level, nlevel)

    def levelOrder(self):
        if self.isEmpty():
            return ""
        else:
            level = Queue()
            level.enqueue(Node(self.root))
            nlevel = 1
            return self.levelOrderCall(level, nlevel)

    def inOrderCall(self, ptr:NodeT) -> str:
        if ptr is None:
            return ""
        else:
            result = ""
            result += self.inOrderCall(ptr.left)
            result += str(ptr.key) + " "
            result += self.inOrderCall(ptr.right)
            return result

    def inOrder(self):
        return self.inOrderCall(self.root)

    def inOrderInvCall(self, ptr:NodeT) -> str:
        if ptr is None:
            return ""
        else:
            result = ""
            result += self.inOrderInvCall(ptr.right)
            result += str(ptr.key) + " "
            result += self.inOrderInvCall(ptr.left)
            return result

    def inOrderInv(self):
        return self.inOrderInvCall(self.root)

    def preOrderCall(self, ptr):
        if ptr is None:
            return ""
        else:
            result = ""
            result += str(ptr.key) + " "
            result += self.preOrderCall(ptr.left)
            result += self.preOrderCall(ptr.right)
            return result

    def preOrder(self):
        return self.preOrderCall(self.root)

    def posOrderCall(self, ptr):
        if ptr is None:
            return ""
        else:
            result = ""
            result += self.posOrderCall(ptr.left)
            result += self.posOrderCall(ptr.right)
            result += ptr.key + " "
            return result

    def posOrder(self):
        return self.posOrderCall(self.root)

    def distance(self, node, ptr):
        if self.isNode(node):
            if node == ptr:
                return 1
            else:
                if node > ptr:
                    return 1 + self.distance(node, ptr.right)
                else:
                    return 1 + self.distance(node, ptr.left)
        else:
            raise Exception("There is no node " + str(node.key))

    def minDistanceNodesCall(self, node1, node2, ptr):
        if node1 < ptr and node2 < ptr:
            return self.minDistanceNodesCall(node1, node2, ptr.left)
        elif node1 > ptr and node2 > ptr:
            return self.minDistanceNodesCall(node1, node2, ptr.right)
        else:
            return self.distance(node1, ptr) + self.distance(node2, ptr) - 1

    def minDistanceNodes(self, node1, node2):
        if not self.isEmpty():
            return self.minDistanceNodesCall(node1, node2, self.root)
        else:
            raise Exception("Tree is empty")
