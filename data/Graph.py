
from data.HashTable import HashTable
from data.Node import Node
from data.LinkedList import LinkedList
from data.StaticList import StaticList
from data.Queue import Queue


class Graph:

    def __init__(self) -> None:
        self.adj_list:HashTable = HashTable()

    def __str__(self) -> str:
        return_str = ""
        size = self.adj_list.number_key()
        acc = 0
        for hash in self.adj_list:
            hash:HashTable.HashData
            if acc == size-1:
                return_str += f"{hash.key} -> {hash.value}"
            else:
                return_str += f"{hash.key} -> {hash.value} \n"
            acc += 1
        return return_str
    
    def find_vertex(self, vertex):
        return self.adj_list.find(vertex)
    
    def find_edge(self, vertex1, vertex2):
        is_vertex1 = self.adj_list.find(vertex1)
        if is_vertex1:
            list_vertex1:LinkedList = self.adj_list.get(vertex1)
            if not list_vertex1.isEmpty() and list_vertex1.find(Node(vertex2)):
                return True
        return False

    def add_vertex(self, vertex):
        is_vertex = self.adj_list.find(vertex)
        if not is_vertex:
            self.adj_list.insert(vertex, LinkedList())

    def remove_vertex(self, vertex_remove):
        is_vertex = self.adj_list.find(vertex_remove)
        if is_vertex:
            self.adj_list.remove(vertex_remove)
            for hash in self.adj_list:
                current_edges:LinkedList = hash.value
                if current_edges.find(Node(vertex_remove)):
                    current_edges.delete(Node(vertex_remove))

    def add_edge(self, vertex1,vertex2):
        is_vertex1 = self.adj_list.find(vertex1)
        is_vertex2 = self.adj_list.find(vertex2)
        if is_vertex1 and is_vertex2:
            list_vertex1:LinkedList = self.adj_list.get(vertex1)
            list_vertex2:LinkedList = self.adj_list.get(vertex2)
            if vertex1 == vertex2:
                if list_vertex1.isEmpty() or not list_vertex1.find(Node(vertex2)):
                    list_vertex1.pushBack(Node(vertex2)) 
            else:
                if list_vertex1.isEmpty() or not list_vertex1.find(Node(vertex2)):
                    list_vertex1.pushBack(Node(vertex2)) 
                if list_vertex2.isEmpty() or not list_vertex2.find(Node(vertex1)):
                    list_vertex2.pushBack(Node(vertex1)) 

    def remove_edge(self, vertex1, vertex2):
        is_vertex1 = self.adj_list.find(vertex1)
        is_vertex2 = self.adj_list.find(vertex2)
        if is_vertex1 and is_vertex2:
            edges_list1:LinkedList = self.adj_list.get(vertex1)
            edges_list2:LinkedList = self.adj_list.get(vertex2)

            if edges_list1.find(Node(vertex2)):
                edges_list1.delete(Node(vertex2))
            if edges_list2.find(Node(vertex1)):
                edges_list2.delete(Node(vertex1))

    def get_neighbors(self, vertex) -> list:
        is_vertex = self.adj_list.find(vertex)
        if is_vertex:
            list_vertex:LinkedList = self.adj_list.get(vertex)
            return list_vertex.to_list()
        else:
            raise KeyError("Key doesn't exists")
        
    #Breadth-First Search
    def bfs(self, origin_vertex) -> str:
        is_visited = HashTable()

        for hash in self.adj_list:
            hash:HashTable.HashData # {vertex:list_edges}
            is_visited.insert(hash.key, False)
        
        queue = Queue()
        queue.enqueue(Node(origin_vertex))
        is_visited.set(origin_vertex, True)

        to_return = ""

        while not queue.isEmpty():
            cur_vertex = queue.dequeue()
            to_return += str(cur_vertex) + " "

            neighbors_list:LinkedList = self.adj_list.get(cur_vertex)
            for neighbor in neighbors_list:
                if not is_visited.get(neighbor):
                    queue.enqueue(Node(neighbor))
                    is_visited.set(neighbor, True)
        return to_return
    
    #Depth-First Search
    def dfs(self, origin_vertex) -> str:
        is_visited = HashTable()

        for hs in self.adj_list:
            #hs = {vertex: list_edge}
            is_visited.insert(hs.key, False)

        self.dfs_path = []

        self.dfs_recursive(origin_vertex, is_visited)

        return str(self.dfs_path)

    def dfs_recursive(self, cur_vertex, is_visited:HashTable) -> str:
        is_visited.set(cur_vertex, True)

        self.dfs_path.append(cur_vertex)

        neighbors:LinkedList = self.adj_list.get(cur_vertex)
        for neighbor in neighbors:
            if not is_visited.get(neighbor):
                self.dfs_recursive(neighbor, is_visited)

    def bfs_shortest_path(self, origin_vertex, final_vertex):
        visited:LinkedList = LinkedList()
        queue = Queue()
        queue.enqueue(Node((origin_vertex, [])))

        while not queue.isEmpty():
            current_vertex, path = queue.dequeue()

            if current_vertex == final_vertex:
                return path + [current_vertex]

            visited.pushBack(Node(current_vertex))

            neighbors:LinkedList = self.adj_list.get(current_vertex)
            for neighbor in neighbors:
                if not visited.find(Node(neighbor)):
                    queue.enqueue(Node((neighbor, path + [current_vertex])))

        return None