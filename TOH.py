def TOI(n, A, B, C):
    if n>0:
        TOI(n-1, A, C, B)
        print("From", A, "to", C)
        TOI(n-1, B, A, C)

TOI(3, 1, 2, 3)