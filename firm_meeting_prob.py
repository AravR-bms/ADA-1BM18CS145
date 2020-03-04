
def max_meetings(S, F):
    i = 0
    print(i)

    for j in range(len(F)):
        if S[j] >= F[i]:
            print(j),
            i = j


s = [1, 5, 1, 5, 8, 5]
f = [3, 6, 6, 7, 9, 9]
max_meetings(s, f)
