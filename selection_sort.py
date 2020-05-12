
def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


test_arr = [8, 3, 63, 45, 23, 89, 23, 56, 0, 23, 5, 8]
selection_sort(test_arr)
print("Sorted:", test_arr)
