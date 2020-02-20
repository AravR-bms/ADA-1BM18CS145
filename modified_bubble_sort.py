def motified_bubble_sort(a, n):
    for j in range(1, n):
        flag = False
        for i in range(0, n-j):
            if a[i] > a[i+1]:
                # swap
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

                flag = True

        if flag == False:
            break


# DRIVER CODE
test_arr = [1, 2, 3, 4, 5, 6, 7]
motified_bubble_sort(test_arr, len(test_arr))
print(test_arr)

test_arr = [2, 6, 4, 7, 1, 9, 3, 2, 5, 0]
motified_bubble_sort(test_arr, len(test_arr))
print(test_arr)
