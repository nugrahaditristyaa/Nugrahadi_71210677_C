class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set() 

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ",end = '')
        # tulis kode Anda di bawah sini
        for key, value in self._data.items():
            print(key, end = ' ')
    
    def edge(self): #mencetak seluruh edge
        print("\nSeluruh Edge = ",end = '')
        # tulis kode Anda di bawah sini
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
                    
        for item in listEdge:
            print(item, end = ' ')

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self,node):
        # silahkan tulis kode Anda di bawah ini 
        print("\nTraversing BFS = ",end = '')
        visited = []
        queue = [] 
        visited.append(node)
        queue.append(node)
        while queue:
            x = queue.pop(0) 
            print (x, end = " ")

            for tetangga in self._data[x]:
                if tetangga not in visited:
                    visited.append(tetangga)
                    queue.append(tetangga)

    def findPath(self, x, y):
        visited = []
        self.dfs(x, y, visited) 

    def dfs(self, node, y, visited):
        visited.append(node)
        if node == y:
            print(visited)
        else:
            for item in self._data[node]:
                if item not in visited:
                    self.dfs(item, y, visited)

# silahkan buat graph seperti pada soal
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('d', 'e')
graph.addEdge('c', 'e')
graph.addEdge('c', 'g')
graph.addEdge('e', 'f')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs('a')