from data.StaticList import StaticList


class DisjointSet:
    def __init__(self, size):
        self.parent = StaticList(size)
        self.rank = StaticList(size)

    def make_set(self):
        for i in range(self.parent.size):
            self.parent.list[i] = i
            self.parent.index = i + 1
            self.rank.list[i] = 0
            self.rank.index = i + 1

    def make_set_un(self, i):
        self.parent.list[i] = i
        self.rank.list[i] = 0

    def find_slow(self, i):
        while i != self.parent.list[i]:
            i = self.parent.list[i]
        return i

    def find(self, i):
        if i != self.parent.list[i]:
            self.parent.list[i] = self.find(self.parent.list[i])
        return self.parent.list[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank.list[i_id] > self.rank.list[j_id]:
            self.parent.list[j_id] = i_id
        else:
            self.parent.list[i_id] = j_id
            if self.rank.list[i_id] == self.rank.list[j_id]:
                self.rank.list[j_id] = self.rank.list[j_id] + 1
