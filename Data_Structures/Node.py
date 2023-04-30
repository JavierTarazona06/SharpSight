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