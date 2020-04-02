def get_fib(n):
    first, second, third = 0, 1, 1
    list = []
    while third <= n + 1:
        list.append(third)
        first, second = second, third
        third = first + second
    return list


arr = list(map(int, input("Enter array: ").split(" ")))
n = len(arr)
fibs = get_fib(n)

jumps = [n] * (n + 1)
arr.append(1)
for i in range(n + 1):
    if arr[i] == 1:
        for fib in fibs:
            if i - fib == -1:
                jumps[i] = 1
            elif i - fib > -1:
                jumps[i] = min(jumps[i], jumps[i - fib] + 1)

print("Jumps: " + str(jumps[-1]))
