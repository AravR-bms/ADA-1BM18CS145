def can_finish(tasks, prerequisites):
    mat = {}
    for i in range(tasks):
        mat[i] = {}

    visited = [False for i in range(tasks)]
    repeated = [False for i in range(tasks)]
    stack = []

    for u, v in prerequisites:
        mat[v][u] = 1

    def topologicalSort(node):
        visited[node] = True
        repeated[node] = True

        for child in mat[node]:
            if not visited[child]:
                if topologicalSort(child):
                    return True
            elif repeated[child]:
                return True

        stack.append(node)
        repeated[node] = False
        return False

    cycle = False
    for node in range(tasks):
        if not visited[node]:
            if topologicalSort(node):
                cycle = True
                break

    return not cycle


print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))

