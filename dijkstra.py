def printSolution(dist, vertices):
    print("Vertex \tDistance from Source")
    for node in range(vertices):
        print(node, "\t", dist[node])


def minDistance(dist, sptSet, vertices):
    min = 999999  # a big value
    # min_index = 0
    for v in range(vertices):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def dijkstra(src, graph, vertices):
    dist = [999999] * vertices
    dist[src] = 0
    sptSet = [False] * vertices

    for cout in range(vertices):
        u = minDistance(dist, sptSet, vertices)
        sptSet[u] = True

        for v in range(vertices):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    printSolution(dist, vertices)


# DRIVER CODE
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
dijkstra(0, graph, 9)
