from collections import deque, defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0  # reverse capacity is initially 0

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

        return max_flow


# Number of vertices in the graph
V = 9  # S, A, B, C, D, E, F, G, T

# Create a graph given in the above diagram
g = Graph(V)
g.add_edge(0, 1, 6)  # S to A
g.add_edge(0, 2, 1)  # S to B
g.add_edge(0, 3, 10)  # S to C
g.add_edge(1, 4, 4)  # A to D
g.add_edge(1, 5, 1)  # A to E
g.add_edge(1, 2, 2)  # A to B
g.add_edge(2, 5, 20)  # B to E
g.add_edge(3, 2, 2)  # C to B
g.add_edge(3, 6, 5)  # C to F
g.add_edge(4, 7, 5)  # D to G
g.add_edge(4, 5, 2)  # D to E
g.add_edge(5, 7, 10)  # E to G
g.add_edge(5, 6, 6)  # E to F
g.add_edge(6, 7, 4)  # F to T
g.add_edge(7, 8, 12)  # G to T

source = 0  # S
sink = 7   # T

print("The maximum possible flow is:", g.edmonds_karp(source, sink))
