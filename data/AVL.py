from data.BST import BST
from data.NodeT import NodeT


class AVL(BST):
    def __init__(self):
        super().__init__()

    def rotateRight(self, node_original):
        if node_original is None or node_original.left is None:
            return node_original
        else:
            new_parent = node_original.left
            node_original.left = new_parent.right
            new_parent.right = node_original
            if self.root == node_original:
                self.root = new_parent
            return new_parent

    def rotateLeft(self, node_original):
        if node_original is None or node_original.right is None:
            return node_original
        else:
            new_parent = node_original.right
            node_original.right = new_parent.left
            new_parent.left = node_original
            if self.root == node_original:
                self.root = new_parent
            return new_parent

    def rotateDoubleToRight(self, node_or):
        node_or.left = self.rotateLeft(node_or.left)
        return self.rotateRight(node_or)

    def rotateDoubleToLeft(self, node_or):
        node_or.right = self.rotateRight(node_or.right)
        return self.rotateLeft(node_or)

    def factorBalance(self, ptr):
        return self.heightCall(ptr.left) - self.heightCall(ptr.right)

    def insertCall(self, num, ptr):
        if ptr is None:
            ptr = NodeT(num)
        else:
            if num < ptr.key:
                ptr.left = self.insertCall(num, ptr.left)
            elif num > ptr.key:
                ptr.right = self.insertCall(num, ptr.right)
            else:
                print("El elemento", num, "ya está en el árbol!")
        factorBalance = self.factorBalance(ptr)
        if factorBalance > 1 and num > ptr.left.key:
            ptr = self.rotateDoubleToRight(ptr)
        if factorBalance > 1 and num < ptr.left.key:
            ptr = self.rotateRight(ptr)
        if factorBalance < -1 and num < ptr.right.key:
            ptr = self.rotateDoubleToLeft(ptr)
        if factorBalance < -1 and num > ptr.right.key:
            ptr = self.rotateLeft(ptr)
        return ptr

    def insert(self, num):
        self.root = self.insertCall(num, self.root)

    def insertRepCall(self, num, ptr):
        if ptr is None:
            ptr = NodeT(num)
        else:
            if num < ptr.key:
                ptr.left = self.insertRepCall(num, ptr.left)
            elif num >= ptr.key:
                ptr.right = self.insertRepCall(num, ptr.right)
        factorBalance = self.factorBalance(ptr)
        if factorBalance > 1 and num > ptr.left.key:
            ptr = self.rotateDoubleToRight(ptr)
        if factorBalance > 1 and num < ptr.left.key:
            ptr = self.rotateRight(ptr)
        if factorBalance < -1 and num < ptr.right.key:
            ptr = self.rotateDoubleToLeft(ptr)
        if factorBalance < -1 and num > ptr.right.key:
            ptr = self.rotateLeft(ptr)
        return ptr

    def insertRep(self, num):
        self.root = self.insertRepCall(num, self.root)

    def deleteCall(self, toDelete, ptr):
        if ptr is not None:
            if toDelete.key < ptr.key:
                ptr.left = self.deleteCall(toDelete, ptr.left)
            elif toDelete.key > ptr.key:
                ptr.right = self.deleteCall(toDelete, ptr.right)
            else:
                # Caso de hojas o un hijo
                if ptr.left is None:
                    return ptr.right
                if ptr.right is None:
                    return ptr.left
                # Caso con los dos hijos
                sig = self.next(ptr)
                ptr.key = sig.key
                ptr.right = self.deleteCall(sig, ptr.right)
            factorBalance = self.factorBalance(ptr)
            if factorBalance > 1 and toDelete.key > ptr.left.key:
                ptr = self.rotateDoubleToRight(ptr)
            if factorBalance > 1 and toDelete.key < ptr.left.key:
                ptr = self.rotateRight(ptr)
            if factorBalance < -1 and toDelete.key < ptr.right.key:
                ptr = self.rotateDoubleToLeft(ptr)
            if factorBalance < -1 and toDelete.key > ptr.right.key:
                ptr = self.rotateLeft(ptr)
            return ptr
        else:
            return None

    def delete(self, toDelete):
        if self.isNode(toDelete):
            self.root = self.deleteCall(toDelete, self.root)
        else:
            raise Exception("Node not in tree")