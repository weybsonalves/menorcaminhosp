from random import randint
from graph_utils import make_graph, dijkstra, bellmanford


def validate(graph):
    vertexes = list(graph.adjacency_list.keys())
    for _ in range(1000):
        i = randint(0, len(vertexes)-1)
        j = randint(0, len(vertexes)-1)
        if dijkstra(graph, vertexes[i], vertexes[j]) != bellmanford(graph, vertexes[i], vertexes[j]):
            return False
    return True


if __name__ == '__main__':
    g = make_graph('municipios_sp.txt', 'distancias_municipios_sp.txt')
    print(validate(g))
