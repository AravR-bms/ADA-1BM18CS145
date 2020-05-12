def gen():
    while True:
        yield False


def johnson_trotter(res, inv, i, tot):
    d = -1
    while True:
        j = inv[i]
        if res[j] < res[j + d]:
            d = -d
            yield next(tot[i - 1])
        else:
            res[j], res[j + d] = res[j + d], res[j]
            inv[i] += d
            inv[res[j]] -= d
            yield True


def setup(n):
    res = [n + 2] + [i for i in range(1, n + 1)] + [n + 2]
    inv = res[:-1]

    tot = [gen()]
    tot.extend(johnson_trotter(res, inv, i + 1, tot) for i in range(n))
    tot += [gen()]

    lead_tot = tot[-2]
    return res, lead_tot


def permutations(n):
    res, lead_tot = setup(n)
    yield res[1:-1]
    while next(lead_tot):
        yield res[1:-1]


# Driver
jt = list(permutations(4))
for el in jt:
    print(el)
print("Length:", len(list(permutations(4))))
