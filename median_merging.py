def get_median(arr1, arr2, n):

    if n == 0:
        return -1

    elif n == 1:
        return (arr1[0]+arr2[1])/2

    elif n == 2:
        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2

    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        if m1 > m2:
            if n % 2 == 0:
                return get_median(arr1[:int(n / 2) + 1],
                                  arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return get_median(arr1[:int(n / 2) + 1],
                                  arr2[int(n / 2):], int(n / 2) + 1)

        else:
            if n % 2 == 0:
                return get_median(arr1[int(n / 2 - 1):],
                                  arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return get_median(arr1[int(n / 2):],
                                  arr2[0:int(n / 2) + 1], int(n / 2) + 1)


def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n/2)]


arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
print(int(get_median(arr1, arr2, len(arr1))))
