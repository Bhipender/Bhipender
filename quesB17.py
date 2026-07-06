# 17.Create an undirected graph with the following edges:
# * A– B
# * A– C
# * B– D
# * C– D
# Display the adjacency list of the graph.


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])


graph1= Graph()

graph1.add_edge('A', 'B')
graph1.add_edge('A', 'C')
graph1.add_edge('B', 'D')
graph1.add_edge('C', 'D')

print("Adjacency List:")
graph1.display()