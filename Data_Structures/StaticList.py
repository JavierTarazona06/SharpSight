from typing import TypeVar, Generic

T = TypeVar('T')

class Error(Exception):
    pass

class StaticList(Generic[T]):
    size:int = None
    list: list = None
    index : int = None
    positionFound : int = None

    def __init__(self, size:int):
        self.size = size
        self.list = []
        for i in range(0,size):
            self.list.append(None)
        self.index = 0

    def pushFront(self,key:T):
        if (self.full()):
            raise Error("Fail pushFront. La lista esta llena. No se pueden guardar más datos")
        else :
            if (self.empty()):
                self.list[0] = key
            else :
                for i in range (self.index,0,-1):
                    self.list[i] = self.list[i-1]
                self.list[0] = key
            self.index += 1

    def topFront(self) -> T:
        if (self.empty()):
            raise Error("Fail topFront. La lista esta vacía")
        else:
            return self.list[0]

    def popFront(self):
        if (self.empty()):
            raise Error("Fail popFront. La lista esta vacía")
        else:
            for i in range(0,self.index-1):
                self.list[i] = self.list[i+1]
            self.index -= 1

    def pushBack(self,key:T):
        if (self.full()):
            raise Error("Fail pushBack. La lista esta llena. No se pueden guardar más datos");
        else:
            self.list[self.index] = key
            self.index += 1

    def topBack(self) -> T:
        if (self.empty()):
            raise Error("Fail topBack. La lista esta vacía")
        else :
            return self.list[self.index-1]

    def popBack(self):
        if (self.empty()):
            raise Error("Fail popBack. La lista esta vacía")
        else:
            self.index -= 1

    def full(self):
        return self.size ==self.index

    def empty(self):
        return self.index==0

    def __str__(self):
        if self.empty():
            return ""
        elif (self.size==1):
            return str(self.list[0])
        else:
            list = ""
            a = 0
            for i in range(0,self.index-1):
                list += str(self.list[i]) + " "
                a = i
            list += str(self.list[a+1])
            return list

    def find(self, key:T) -> bool:
        found:bool = False
        if (self.empty()):
            raise Error("Fail find. La lista esta vacia");
        else :
            for i in range(0,self.index):
                if (self.list[i] == key):
                    found = True
                    self.positionFound = i
                    i = self.index
                    break
        return found

    def findPosition(self,key:int) -> int:
        isThere:bool = self.find(key)
        if (self.empty()):
            raise Error("Fail find. La lista esta vacia")
        elif (not isThere):
            raise Error("Fail findPosition. Key no esta en la lista")
        else:
            return self.positionFound

    def erase(self, key:int):
        if (self.empty()):
            raise Error("Fail erase. La lista esta vacia")
        elif (not self.find(key)):
            raise Error("Fail: Key no esta en la lista")
        else:
            pos = self.positionFound
            for i in range(pos,self.index-1):
                self.list[i] = self.list[i + 1]
            self.index -= 1