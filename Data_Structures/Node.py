from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):

    key = None
    next = None

    # Constructor
    def __init__(self, data:T):
        self.key = data
        self.next = None

    # Métodos
    def get_data(self) -> T:
        return self.key

    def get_next(self):
        return self.next

    def update_key(self, data):
        self.key = data

    def __str__(self):
        return self.key