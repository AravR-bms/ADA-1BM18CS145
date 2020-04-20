def LIS(arr):
    n = len(arr)
    i, j, max_len = 0, 0, 0

    lst = [1]*(n)

    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and lst[i] < lst[j] + 1):
                lst[i] = lst[j] + 1

    for i in range(n):
        if max_len < lst[i]:
            max_len = lst[i]

    return max_len


# DRIVER CODE
arr = [23, 12, 67, 22, 34, 54, 12, 57, 21, 47, 26, 28, 83]
print("Length is", LIS(arr))
