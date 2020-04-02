import numpy as np
import copy

n = int(input('Enter number of vertices: '))
adj_matrix = np.zeros((n, n))
# print(adj_mat)

print("Adjacency Matrix :")
for i in range(n):
    adj_matrix[i] = list(map(int, input().split()))
# print(adj_mat)

res_matrix = copy.deepcopy(adj_matrix)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if res_matrix[i][j] != 1 and res_matrix[i][k] == 1 and res_matrix[k][j] == 1:
                res_matrix[i][j] = 1

print("Adj Matrix:\n", adj_matrix)
print("Res Matrix:\n", res_matrix)
