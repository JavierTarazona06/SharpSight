class NodeT:
    def __init__(self, data):
        self.key = data
        self.right = None
        self.left = None

    def getData(self):
        return self.key

    def updateKey(self, data):
        self.key = data

    def __str__(self):
        if self.key is None:
            return "-"
        else:
            return str(self.key)

    def compareTo(self, otherNode):
        return self.key.compareTo(otherNode.key)

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __eq__(self, other):
        return self.key == other.key
