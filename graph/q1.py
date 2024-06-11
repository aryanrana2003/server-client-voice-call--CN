from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    residual_graph = [row[:] for row in graph]

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Graph based on the image
graph = [
    # S  A  B  C  D  E  F  G  T
    [0, 6, 1,10, 0, 0, 0, 0, 0],  # S
    [0, 0, 2, 0, 4, 0, 0, 0, 0],  # A
    [0, 0, 0, 2, 0,20, 0, 0, 0],  # B
    [0, 0, 0, 0, 0, 0, 5, 0, 0],  # C
    [0, 0, 0, 0, 0, 2, 0, 5, 0],  # D
    [0, 0, 0, 0, 0, 0, 6, 0,10],  # E
    [0, 0, 0, 0, 0, 0, 0, 0, 4],  # F
    [0, 0, 0, 0, 0, 0, 0, 0,12],  # G
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # T
]

source = 0  # S
sink = 8   # T

print(f"The maximum possible flow is {ford_fulkerson(graph, source, sink)}")
