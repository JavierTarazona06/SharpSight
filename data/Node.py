from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):

    key = None
    next = None
    prev = None

    # Constructor
    def __init__(self, data:T):
        self.key = data
        self.next = None
        self.prev = None

    # Métodos
    def get_data(self) -> T:
        return self.key

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def update_key(self, data):
        self.key = data

    def __str__(self):
        return str(self.key)

    def __lt__(self, other_node):
        return self.key < other_node.key

    def __le__(self, other_node):
        return self.key <= other_node.key

    def __eq__(self, other_node):
        try:
            return self.key == other_node.key
        except AttributeError as e:
            return False

    def __gt__(self, other_node):
        return self.key > other_node.key

    def __ge__(self, other_node):
        return self.key >= other_node.key