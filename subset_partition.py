
def subset_partition(arr):
    tot = 0
    i, j = 0, 0
    tot = sum(arr)

    if tot % 2 != 0:
        return False

    part = [[True for i in range(len(arr) + 1)]
            for j in range(tot // 2 + 1)]

    for i in range(0, len(arr) + 1):
        part[0][i] = True

    for i in range(1, tot // 2 + 1):
        part[i][0] = False

    for i in range(1, tot // 2 + 1):
        for j in range(1, len(arr) + 1):
            part[i][j] = part[i][j - 1]
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])

    # print(part[tot // 2][len(arr)])
    return part[tot // 2][len(arr)]


arr = [3, 1, 1, 2, 2, 1]

if subset_partition(arr) == True:
    print("Can be divided")
else:
    print("Cannot be divided")
