from datetime import *
import time
from typing import TypeVar, Generic

from StaticList import StaticList

T = TypeVar('T')

class Error(Exception):
    pass

class DynamicList(StaticList):

    def __init__(self):
        super().__init__(1)

    def pushFront(self,key:T):
        if (self.full()):
            self.size *= 2
            newList = []
            for j in range(0,self.index):
                newList.append(self.list[j])
            for j in range(self.index,self.size):
                newList.append(None)
            self.list = newList
            self.pushFront(key)
        else:
            if (self.empty()):
                self.list[0] = key
            else:
                for i in range(self.index,0,-1):
                    self.list[i] = self.list[i-1]
                self.list[0] = key
            self.index += 1

    def pushBack(self,key:T):
        if (self.full()):
            self.size *= 2
            newList = []
            for j in range(0,self.index):
                newList.append(self.list[j])
            for j in range(self.index,self.size):
                newList.append(None)
            self.list = newList
            self.pushBack(key)
        else:
            self.list[self.index] = key
            self.index += 1

    def insert(self, pos,data):
        if pos< 0 or pos >= self.index:
            raise IndexError('Index out of range')
        if self.full():
            self.size *= 2
            newList = []
            for j in range(0,self.index):
                newList.append(self.list[j])
            for j in range(self.index,self.size):
                newList.append(None)
            self.list = newList
            self.insert(pos,data)
        else:
            for i in range(self.index, pos, -1):
                self.list[i] = self.list[i - 1]
            self.list[pos] = data
            self.index += 1

    def insertOrdered(self,data):
        if self.empty():
            self.pushBack(data)
        elif self.full():
            self.size *= 2
            newList = []
            for j in range(0,self.index):
                newList.append(self.list[j])
            for j in range(self.index,self.size):
                newList.append(None)
            self.list = newList
            self.insertOrdered(data)
        else:
            i = 0
            while i<self.index and self.list[i]<data:
                i+=1
            for j in range (self.index,i,-1):
                self.list[j] = self.list[j-1]
            self.list[i] = data
            self.index+=1