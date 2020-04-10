



def primMST(graph, vertices):
    
    key = [99999] * vertices
    parent = [None] * vertices

    key[0] = 0
    mstSet = [False] * vertices
    parent[0] = -1

    for _ in range(vertices):

        min = 99999
        for v in range(vertices):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        u = min_index
        mstSet[u] = True

        for v in range(vertices):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge\tWeight")
    for i in range(1, vertices):
         print(f"{parent[i]} - {i}\t {graph[i][parent[i]]}")



vertices = 5
graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

primMST(graph, vertices)