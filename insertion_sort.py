
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


test_arr = [3, 4, 6, 2, 6, 8, 4, 2, 6, 9, 3, 7, 0, 1, 3, 3]
insertion_sort(test_arr)
print(test_arr)
