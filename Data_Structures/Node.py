from typing import TypeVar, Generic

T = TypeVar('T')

class Error(Exception):
    pass

class Node(Generic[T]):

    key = None
    next = None

    # Constructor
    def __init__(self, data):
        self.key = data
        self.next = None

    # Métodos
    def get_data(self):
        return self.key

    def get_next(self):
        return self.next

    def update_key(self, data):
        self.key = data

    def __str__(self):
        return self.key