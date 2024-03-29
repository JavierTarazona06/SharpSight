from typing import TypeVar, Generic

T = TypeVar('T')

class Error(Exception):
    pass

class OrderedList(Generic[T]):
    size:int = None #Capacidad
    list: list = None
    index : int = None #Número de elementos+1
    positionFound : int = None

    def __init__(self):
        size = 1
        self.size = size
        self.list = []
        for i in range(0,size):
            self.list.append(None)
        self.index = 0

    def topFront(self) -> T:
        if (self.empty()):
            raise Error("Fail topFront. La lista esta vacía")
        else:
            return self.list[0]


    def topBack(self) -> T:
        if (self.empty()):
            raise Error("Fail topBack. La lista esta vacía")
        else :
            return self.list[self.index-1]

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

    def find(self,key):
        if self.empty():
            raise Exception("Empty List")
        else:
            return not self.findPosition(key)==-1

    def findPosition(self, key):
        if self.empty():
            raise Exception("Empty List")
        else:
            return self.binarySearch(0,self.index-1,key)

    def binarySearch(self,inicio,fin,key):
        if fin>=inicio:
            mid = (fin+inicio)//2
            if self.list[mid] == key:
                return mid
            elif self.list[mid] > key:
                return self.binarySearch(inicio,mid-1,key)
            else:
                return self.binarySearch(mid+1,fin,key)
        else:
            return -1

    def delete(self, key:T):
        if (self.empty()):
            raise Error("Fail erase. La lista esta vacia")
        elif (not self.find(key)):
            raise Error("Fail: Key no esta en la lista")
        else:
            pos = self.positionFound
            for i in range(pos,self.index-1):
                self.list[i] = self.list[i + 1]
            self.index -= 1

    def insert(self,data):
        if self.empty():
            self.list[self.index] = data
            self.index += 1
        elif self.full():
            self.size *= 2
            newList = []
            for j in range(0, self.index):
                newList.append(self.list[j])
            for j in range(self.index, self.size):
                newList.append(None)
            self.list = newList
            self.insert(data)
        else:
            i = 0
            while i<self.index and self.list[i]<data:
                i+=1
            if not self.list[i]==data:
                for j in range (self.index,i,-1):
                    self.list[j] = self.list[j-1]
                self.list[i] = data
                self.index+=1