def vertex_cover(graph):
    cover = set()
    edges = {frozenset((u, v)) for u in graph for v in graph[u]}
    
    while edges:
        u, v = max(edges, key=lambda e: len(graph[list(e)[0]]) + len(graph[list(e)[1]]))
        cover.add(u)
        cover.add(v)
        
        to_remove = {e for e in edges if u in e or v in e}
        edges -= to_remove
        
    return cover

# Graph based on the image
graph = {
    'S': {'A', 'B', 'C'},
    'A': {'B', 'D'},
    'B': {'C', 'E'},
    'C': {'F'},
    'D': {'E', 'G'},
    'E': {'F', 'T'},
    'F': {'T'},
    'G': {'T'},
    'T': set()
}

cover = vertex_cover(graph)
print(f"The vertex cover is: {cover}")
