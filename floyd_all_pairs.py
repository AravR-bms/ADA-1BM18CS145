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
            res_matrix[i][j] = min(
                res_matrix[i][j], res_matrix[i][k] + res_matrix[k][j])

print("Adj Matrix:\n", adj_matrix)
print("Res Matrix:\n", res_matrix)
