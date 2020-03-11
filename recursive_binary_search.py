

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:

        return -1


arr = [1, 5, 8, 12, 15, 18, 26, 38, 49, 55, 57, 66, 79, 90]
x1 = 55
x2 = 68

result = binary_search(arr, 0, len(arr)-1, x1)
print(result)

result = binary_search(arr, 0, len(arr)-1, x2)
print(result)
