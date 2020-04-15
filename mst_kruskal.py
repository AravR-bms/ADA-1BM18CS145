def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskal_mst(graph, vertices):

    result = []
    parent = []
    rank = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])

    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    while e < vertices - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    print("Edges in the constructed MST")
    for u, v, weight in result:
        print("%d -- %d == %d" % (u, v, weight))


vertices = 4
graph = [[0, 1, 10],
         [0, 2, 6],
         [0, 3, 5],
         [1, 3, 15],
         [2, 3, 4]]

kruskal_mst(graph, vertices)
