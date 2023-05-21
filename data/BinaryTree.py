class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  #pointer
        self.height = 1
        self.size = 1

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, current, value):
        #check if we have a root node or not
        if self.root == None:
            #creating a new node
            self.root = Node(value)
            self.size += 1
        else:
            if value < current.value:
                #if the value is less than my current value
                if current.left == None:
                    #create a new node in the left, if not is created already
                    current.left = Node(value)
                    current.left.parent = current
                    self.size += 1
                else:
                    self.add(current.left, value)
            else:
                if current.right == None:
                    # create a new node in the right, if not is created already
                    current.right = Node(value)
                    current.right.parent = current
                    self.size += 1
                else:
                    self.add(current.right, value)

    def size(self):
        return self.size
    def visit(self, node):
        print(node.value)

    def preorder(self,current):
        if current is not None:
            self.visit(current)
            self.preorder(current.left)
            self.preorder(current.right)

    def inorder(self, current):
        if current is not None: #if the actual node is null
            self.inorder(current.left)
            self.visit(current)
            self.inorder(current.right)

    def postorder(self,current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            self.visit(current)

    def height(self):#check if root is none
        if self.root != None:
            return self.height(self.root,0)
        else:
            return 0
    def _height (self,current,current_height):
        if current == None: # here we arrived to final to the tree
            return current_height #so we can retunr
        left_height = self.height(current.left, current_height+1)
        right_height = self.height(current.right, current_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self, value, current):
        if value == current.value:
            return True
        elif value < current.value and current.left != None:
            return self._search(value, current.left)
        elif value > current.value and current.right != None:
            return self._search(value, current.right)
        return False

    # it he
    def find(self, value):
        if self.root != None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,current):
        if value == current.value:
            return current
        elif value < current.value and current.left != None:
            return self._find(value,current.left)
        elif value > current.value and current.right != None:
            return self._find(value, current.right)

    def empty(self, root):
        return self.root == None

    # it he
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current):
        if value == current.value:
            return current
        elif value < current.value and current.left != None:
            return self._find(value, current.left)
        elif value > current.value and current.right != None:
            return self._find(value, current.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node is None:
            return

        def min_value(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def max_value(n):
            current = n
            while current.right is not None:
                current = current.right
            return current

        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        number_children = num_children(node)

        if number_children == 0:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
            self.size -= 1  # decrease size after deleting a node

        elif number_children == 1:
            if node.parent is None:
                if node.left is None:
                    self.root = node.right
                else:
                    self.root = node.left
            else:
                if node.right is None:
                    if node.parent.value > node.left.value:
                        node.parent.left = node.left
                    else:
                        node.parent.right = node.left
                else:
                    if node.parent.value > node.right.value:
                        node.parent.left = node.right
                    else:
                        node.parent.right = node.right
            self.size -= 1  # decrease size after deleting a node

        else:
            node_to_delete = min_value(node.right)
            node.value = node_to_delete.value
            self.delete_node(node_to_delete)

    def print_size(self):
        print("Size:", self.size)


# Crear una instancia de la clase BST
bst = BST()

# Agregar los nodos al árbol binario de búsqueda
bst.add(bst.root, 7)
bst.add(bst.root, 5)
bst.add(bst.root, 3)
bst.add(bst.root, 4)
bst.add(bst.root, 6)
bst.add(bst.root, 12)
bst.add(bst.root, 8)
bst.add(bst.root, 13)
bst.add(bst.root,16)


# Imprimir los nodos en orden
bst.inorder(bst.root)

bst.print_size()
print(bst.search(12))
print(bst.delete_value(12))
print(bst.delete_value(7))
print(bst.delete_value(13))
print(bst.search(12))
bst.print_size()
bst.inorder(bst.root)