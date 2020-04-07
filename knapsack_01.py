
def knapsack(max_weight, weight, values):
    K = [[0 for x in range(max_weight+1)] for x in range(len(values)+1)]

    for i in range(len(values)+1):
        for w in range(max_weight+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[len(values)][max_weight]


values = [10, 40, 30, 50]
weight = [5, 4, 6, 3]
max_weight = 10
print(f"Solution: {knapsack(max_weight, weight, values)}")
