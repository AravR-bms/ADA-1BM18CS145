def min_coin_change(change):

    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(coins)
    ans = []

    i = n - 1
    while(i >= 0):
        while (change >= coins[i]):
            change -= coins[i]
            ans.append(coins[i])
        i -= 1

    for i in range(len(ans)):
        print(ans[i], end=" ")


min_coin_change(26)
