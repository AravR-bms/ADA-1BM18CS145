N = 5
ptr = [0 for i in range(501)]


def smallest_range(arr, n, k):
    i, min_val, max_val, min_range, min_element, max_element, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(k + 1):
        ptr[i] = 0

    min_range = 10**9

    while(1):
        minind = -1
        min_val = 10**9
        max_val = -10**9
        flag = 0

        for i in range(k):
            if(ptr[i] == n):
                flag = 1
                break
            if(ptr[i] < n and arr[i][ptr[i]] < min_val):
                minind = i
                min_val = arr[i][ptr[i]]
            if(ptr[i] < n and arr[i][ptr[i]] > max_val):
                max_val = arr[i][ptr[i]]

        if(flag):
            break
        ptr[minind] += 1
        if((max_val-min_val) < min_range):
            min_element = min_val
            max_element = max_val
            min_range = max_element - min_element

    print("The smallest range is [", min_element, max_element, "]")


arr = [[4, 7, 9, 12, 15],
       [0, 8, 10, 14, 20],
       [6, 12, 16, 30, 50]]
k = len(arr)

smallest_range(arr, N, k)
