
def bfs(graph, node):
    visited = []
    queue = []

    print(f"All the nodes of are:")
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)

        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph_test = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}
print("\nFor graph_test:")
bfs(graph_test, 'A')

graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H', 'I'],
    'H': ['J'],
    'I': [],
    'J': ['I']
}
print("\n\nFor graph1:")
bfs(graph1, 'A')

graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': ['C', 'D']
}
print("\n\nFor graph2:")
bfs(graph2, 'A')
