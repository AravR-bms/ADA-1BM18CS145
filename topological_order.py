def topological_order(graph, start):
    seen = set()
    stack = []
    order = []
    q = [start]

    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(topological_order(graph, 'A'))
