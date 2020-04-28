class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def safe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def colour(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m+1):
            if self.safe(v, colour, c) == True:
                colour[v] = c
                if self.colour(m, colour, v+1) == True:
                    return True
                colour[v] = 0

    def coloured_graph(self, m):
        colour = [0] * self.V
        if self.colour(m, colour, 0) == None:
            return False

        print("Colours:")
        for c in colour:
            print(c, end=' ')
        return True


graph = Graph(4)
graph.graph = [[0, 1, 1, 1],
               [1, 0, 1, 0],
               [1, 1, 0, 1],
               [1, 0, 1, 0]]
m = 3
graph.coloured_graph(m)
