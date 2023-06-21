from data.Node import Node
from data.StaticList import StaticList
from data.DynamicList import DynamicList
from data.LinkedList import LinkedList

class HashTable:

    class HashData:

        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value

        def __str__(self) -> str:
            return f"{self.key}: {self.value}"

        def change_value(self, new_value) -> None:
            self.value = new_value

        def __eq__(self, other_hashed) -> bool:
            return self.key==other_hashed.key and self.value==other_hashed.value

    def __init__(self, size=16, alpha=0.75, a=5, b=11, x=2521) -> None:
        #alpha is load factor
        self.lista_hash = StaticList(size)
        self.size = size
        self.alpha = alpha
        self.a = a #Hash function parameters
        self.b = b
        self.x = x

    def __str__(self) -> str:
        list_return = []
        for element_list in self.lista_hash.list:
            if (str(type(element_list)) == "<class 'data.LinkedList.LinkedList'>"):
                element_list:LinkedList
                element_list_str = []
                for e in element_list:
                    e:HashTable.HashData
                    element_list_str.append(str(e))
                list_return.append(element_list_str)
            else:
                list_return.append(element_list)
        return str(list_return)
    
    def __iter__(self):
        self.index_interable:int = 0
        self.list_interable:list = self.to_list()
        return self
    
    def __next__(self):
        if self.index_interable == len(self.list_interable):
            raise StopIteration
        else:
            self.index_interable += 1
            return self.list_interable[self.index_interable-1]

    def to_list(self) -> list:
        index_interable:int = 0
        lista:list = []
        while index_interable < self.size:
            if self.lista_hash.list[index_interable] is not None:
                hash_list:LinkedList = self.lista_hash.list[index_interable]
                index_interable += 1
                for hash in hash_list:
                    lista.append(hash)
            else:
                index_interable += 1
        return lista
    
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_next_prime(self, n):
        next_num = n + 1
        while not self.is_prime(next_num):
            next_num += 1
        return next_num
    
    def hash_function_int(self, key:int) -> int:
        #return key % self.size
        return (((self.a*key)+ self.b) % self.get_next_prime(self.size)) % self.size
    
    def hash_function_str(self, key:str) -> int:
        hash = 0
        for i in range(len(key)-1, -1, -1):
            hash = ((hash * self.x) + ord(key[i])) % self.x % self.size
        return hash
    
    def calculate_hash_str(self, string):
        hash = 0
        for char in string:
            hash = (hash * self.x + ord(char)) % self.x
        return hash
    
    def recalculate_hash_str(self, hash:int, old_char:str, new_char:str):
        hash = (hash - ord(old_char)) % self.x
        hash = ((hash*self.x) + ord(new_char)) % self.x
        return hash
    
    def number_key(self) -> int:
        acc:int = 0
        for hash in self:
            acc += 1
        return acc
    
    def load_factor(self) -> float:
        return self.number_key()/self.size
    
    def rehash(self) -> None:
        load_factor = self.load_factor()
        if load_factor > self.alpha:
            new_hash_table:HashTable = HashTable(size=self.size*2)
            for hash in self:
                hash:HashTable.HashData
                new_hash_table.insert(hash.key, hash.value)
            self.lista_hash = new_hash_table.lista_hash
            self.size = new_hash_table.size
    
    def insert(self, key:int, value:object) -> None:
        if self.find(key):
            self.set(key, value)
        else:
            if (str(type(key))=="<class 'int'>"):
                hash_index = self.hash_function_int(key)
            elif (str(type(key))=="<class 'str'>"):
                hash_index = self.hash_function_str(key)
            data_to_hash:HashTable.HashData = HashTable.HashData(key, value)
            if (self.lista_hash.list[hash_index] == None):
                sub_linked_list = LinkedList()
                sub_linked_list.pushBack(Node(data_to_hash))
                self.lista_hash.list[hash_index] = sub_linked_list
            else:
                sub_linked_list:LinkedList = self.lista_hash.list[hash_index]
                sub_linked_list.pushBack(Node(data_to_hash))
            self.rehash()

    def get(self, key:int)->object:
        if (str(type(key))=="<class 'int'>"):
            hash_index = self.hash_function_int(key)
        elif (str(type(key))=="<class 'str'>"):
            hash_index = self.hash_function_str(key)
        possible_linked_list:LinkedList = self.lista_hash.list[hash_index]
        for hashed_data in possible_linked_list:
            hashed_data:HashTable.HashData
            if hashed_data.key == key:
                return hashed_data.value
        raise KeyError("Key is not in HashTable")

    
    def find(self, key: int) -> bool:
        try:
            self.get(key)
            return True
        except Exception:
            return False
        
    def remove(self, key:int) -> bool:
        value = self.get(key)
        hash_data_to_remove = HashTable.HashData(key, value)
        if (str(type(key))=="<class 'int'>"):
            hash_index = self.hash_function_int(key)
        elif (str(type(key))=="<class 'str'>"):
            hash_index = self.hash_function_str(key)
        elements_linked_list:LinkedList = self.lista_hash.list[hash_index]
        elements_linked_list.delete(Node(hash_data_to_remove))
        if elements_linked_list.isEmpty():
            self.lista_hash.list[hash_index] = None

    def set(self, key:int, value:object) -> None:
        new_hash:HashTable.HashData = HashTable.HashData(key, value)
        if (str(type(key))=="<class 'int'>"):
            hash_index = self.hash_function_int(key)
        elif (str(type(key))=="<class 'str'>"):
            hash_index = self.hash_function_str(key)
        hash_linked_list:LinkedList = self.lista_hash.list[hash_index]
        if hash_linked_list is None:
            raise KeyError("Key is not in HashTable")
        for hash in hash_linked_list:
            hash:HashTable.HashData
            if hash.key == key:
                old_hashed:HashTable.HashData =  hash
                hash_linked_list.replace(Node(old_hashed), Node(new_hash))
                return
            
    def rabin_karp(self, text, pattern):
        if not text or not pattern:
            return []

        n = len(text)
        m = len(pattern)
        if n < m:
            return []

        result = []
        pattern_hash = self.calculate_hash_str(pattern)
        text_hash = self.calculate_hash_str(text[:m])

        # Iterate to look for potential matches
        for i in range(n - m + 1):
            # Check if the actual substrings are equal
            if pattern_hash == text_hash and pattern == text[i:i + m]:
                result.append(i)
            if i < n - m:
                text_hash = self.recalculate_hash_str(text_hash, text[i], text[i + m])

        return result
    
    def proves(self):
        myHash = HashTable()
        myHash.insert(5,"2-5")
        myHash.insert(21,"2-21")
        myHash.insert(37,"2-37")
        myHash.insert(53,"2-53")
        myHash.insert(4,"2-4")
        myHash.insert(16,"2-16")
        myHash.insert(20,"2-20")
        myHash.insert(15,"15-20")
        myHash.insert(46, 32)
        myHash.insert(128, "128-32")
        myHash.insert(149, "149-32")
        myHash.insert(81, "81-32")
        myHash.insert(81, "81-33")
        print(myHash)
        print(myHash.size)
        print(myHash.number_key())
        print(myHash.load_factor())

        myHash.insert("La nueva", "149-32")
        print(myHash)
        print(myHash.size)
        print(myHash.number_key())
        print(myHash.load_factor())

        print(myHash.get("La nueva"))
        
        
        print(myHash.rabin_karp("Samsung 58 Gigas", "58"))