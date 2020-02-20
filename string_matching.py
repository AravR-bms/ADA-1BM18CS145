def string_matching(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(0, n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


# DRIVER CODE
print(string_matching("computer science", "science"))  # 9
print(string_matching("aaaaaaabc", "bc"))  # 7
print(string_matching("aabcaaabc", "bc"))  # 2
print(string_matching("aaaaaaabc", "bcd"))  # -1
