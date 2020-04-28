def subset_sum(set, n, sum):
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False
    if (set[n - 1] > sum):
        return subset_sum(set, n - 1, sum)

    return subset_sum(set, n-1, sum) or subset_sum(set, n-1, sum-set[n-1])


# Driver Code
set = [1, 2, 5, 6, 8]
sum = 9
n = len(set)
if (subset_sum(set, n, sum) == True):
    print("Subset Possible")
else:
    print("Subset Not Possible")
