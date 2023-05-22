from data import Heap


class HeapMin(Heap):

    def __init__(self):
        super().__init__()

    def get_min(self):
        return self.array.list[0]

    def sift_up(self, index):
        if index > 0:
            if self.array.list[self.parent(index)] > self.array.list[index]:
                temp = self.array.list[self.parent(index)]
                self.array.list[self.parent(index)] = self.array.list[index]
                self.array.list[index] = temp
                self.sift_up(self.parent(index))

    def insert(self, key):
        self.array.push_back(key)
        self.sift_up(self.get_size() - 1)

    def sift_down(self, index):
        min_index = index
        try:
            l = self.left_child(index)
            if l < self.get_size() and self.array.list[l] < self.array.list[min_index]:
                min_index = l
        except:
            pass
        try:
            r = self.right_child(index)
            if r < self.get_size() and self.array.list[r] < self.array.list[min_index]:
                min_index = r
        except:
            pass
        if index != min_index:
            temp = self.array.list[index]
            self.array.list[index] = self.array.list[min_index]
            self.array.list[min_index] = temp
            self.sift_down(min_index)

    def extract_min(self):
        result = self.array.list[0]
        last = self.array.list[self.get_size() - 1]
        self.array.list[0] = last
        self.array.index -= 1
        self.sift_down(0)
        return result

    def remove(self, index):
        self.array.list[index] = self.get_min() - 1
        self.sift_up(index)
        self.extract_min()

    def change_priority(self, index, new_value):
        old_value = self.array.list[index]
        self.array.list[index] = new_value
        if new_value < old_value:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def make_heap(self):
        node_internal_index = self.parent(self.get_size() - 1)
        for i in range(node_internal_index, -1, -1):
            self.sift_up(i)

    def heap_sort(self):
        size = self.get_size()
        for i in range(size):
            value = self.extract_min()
            self.array.list[size - (i + 1)] = value
        self.array.index = size
        for i in range(size // 2):
            temp = self.array.list[i]
            self.array.list[i] = self.array.list[size - (i + 1)]
            self.array.list[size - (i + 1)] = temp

    def heap_sort_reverse(self):
        size = self.get_size()
        for i in range(size):
            value = self.extract_min()
            self.array.list[size - (i + 1)] = value
        self.array.index = size


