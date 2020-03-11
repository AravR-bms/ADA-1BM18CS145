def linearSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return linearSearch(arr, l+1, r-1, x)


arr = [1, 5, 8, 12, 15, 18, 26, 38, 49, 55, 57, 66, 79, 90]
x1 = 55
x2 = 68

print(linearSearch(arr, 0, len(arr)-1, x1))
print(linearSearch(arr, 0, len(arr)-1, x2))
