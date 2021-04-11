class Heap:
    def __init__(self, array=[]):
        self.array = array
        self.size = len(array)


    def parent(self, i):
        return (i-1)//2


    def left(self, i):
        return 2*i+1
    
    
    def right(self, i):
        return 2*i+2


    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.size - 1 and self.compare(l, i):
            smaller = l
        else:
            smaller = i
        if r <= self.size - 1 and self.compare(r, smaller):
            smaller = r
        if smaller != i:
            self.array[i], self.array[smaller] = self.array[smaller], self.array[i]
            self.min_heapify(smaller)


    def min_heap_insert(self, key):
        self.array.append(key)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.compare(i, self.parent(i)):
            self.array[i], self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)


    def heap_extract_min(self):
        minimum = self.array[0]
        self.size -= 1
        self.array[0] = self.array[-1]
        self.array.pop()
        self.min_heapify(0)
        return minimum


    def heap_decrease_key(self, i, key):
        if key > self.array[i]:
            return 'ERROR'
        self.array[i] = key
        while i > 0 and self.compare(i, self.parent(i)):
            self.array[i], self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)         


    def compare(self, v1, v2):
        return v1 < v2


class CityHeap(Heap):
    def __init__(self, array=[]):
        super().__init__(array)


    def compare(self, v1, v2):
        return self.array[v1][1] < self.array[v2][1]


class Graph:
    def __init__(self):
        self.adjacency_list = dict()
        self.distance = dict()
        self.predecessor = dict()


    def insert_vertex(self, value):
        self.adjacency_list[value] = []
        self.distance[value] = None
        self.predecessor[value] = None


    def insert_edge(self, v1, v2, w):
        self.adjacency_list[v1].append((v2, w))
        self.adjacency_list[v2].append((v1, w))


def dijkstra(graph, origin, destination):
    for k in graph.adjacency_list.keys():
        graph.distance[k] = 1000000000000000000000000000000000000000000
        graph.predecessor[k] = None
    graph.distance[origin] = 0
    min_heap = CityHeap([(origin, 0)])
    while len(min_heap.array) > 0:
        v, d = min_heap.heap_extract_min()
        if d > graph.distance[v]:
            continue
        for va, w in graph.adjacency_list[v]:
            if graph.distance[va] > d + w:
                graph.distance[va] = d + w
                graph.predecessor[va] = v
                min_heap.min_heap_insert((va, d + w))
    shortest_path = []
    x = destination
    while x != None:
        shortest_path.insert(0, x)
        x = graph.predecessor[x]
    return graph.distance[destination], shortest_path


def bellmanford(graph, origin, destination):
    for k in graph.adjacency_list.keys():
        graph.distance[k] = 1000000000000000000000000000000000000000000
        graph.predecessor[k] = None
    graph.distance[origin] = 0
    for _ in range(len(graph.adjacency_list)-1):
        for v, adj in graph.adjacency_list.items():
            for u, w in adj:
                if graph.distance[u] > graph.distance[v] + w:
                    graph.distance[u] = graph.distance[v] + w
                    graph.predecessor[u] = v
    shortest_path = []
    x = destination
    while x != None:
        shortest_path.insert(0, x)
        x = graph.predecessor[x]
    return graph.distance[destination], shortest_path


def make_graph(vertexes_dir, edges_dir):
    g = Graph()
    idx_to_city = dict()
    with open(vertexes_dir, 'r', encoding='ISO-8859-1') as m:
        for i, line in enumerate(m):
            city = line.replace('\n', '')
            g.insert_vertex(city)
            idx_to_city[i] = city
    with open(edges_dir, 'r', encoding='ISO-8859-1') as db:
        for line in db:
            road = line.replace('\n', '').split()
            g.insert_edge(idx_to_city[int(road[0])], idx_to_city[int(road[1])], float(road[2]))
    return g
