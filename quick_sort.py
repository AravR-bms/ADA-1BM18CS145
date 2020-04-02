def partition(sort_list, low, high):

    i = low - 1
    change = sort_list[high]

    for j in range(low, high):
        if sort_list[j] <= change:
            i += 1
            # swap
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

    # swap
    sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)


def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)


# DRIVER CODE
test_arr = [2, 5, 6, 43, 1, 54, 7, 3, 23, 53, 64, 68, 97, 62, 2, 6, 7]

low = 0
high = len(test_arr) - 1
quick_sort(test_arr, low, high)
print(test_arr)
