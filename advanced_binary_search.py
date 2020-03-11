
#WORKING BI SEARCH
# def bi_search(arr, key):
 
#     l = 0
#     r = len(arr)-1
#     while l <= r:
#         mid = int((l+r)/2)
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             l = mid + 1
#         else: 
#             r = mid - 1

#     return -1

# print(bi_search([1,2,3,3,4,5], 3))

def bi_search(arr, key):
    count  = 0
    left_index = right_index = -1
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = int((l+r)/2)
        if arr[mid] == key:
            for i in range(mid, len(arr)):
                if arr[i] == key and arr[i] <=key:
                    count += 1
                    right_index = i
            for j in range(0, mid):
                if arr[j] == key and arr[j] <=key:
                    count += 1
                    left_index = j         

            #print(count, left_index, right_index)
            print("Count:", count)
            print("Left Index:", left_index, "Right Index:", right_index)
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else: 
            r = mid - 1

    return -1

print("Index", bi_search([1,2,3,3,3,3,4,5], 3))



