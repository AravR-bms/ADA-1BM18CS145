def palindromic_subsequence(txt):
    max_len = 0
    substr = "No substring"
    for i in range(len(txt)-1):
        for j in range(i+1, len(txt)+1):
            str = txt[i:j]
            if str == str[::-1] and len(str) > max_len:
                max_len = len(str)
                substr = str
    return substr


print(palindromic_subsequence("abcdijhhjibdk"))
print(len(palindromic_subsequence("abcdijhhjibdk")))
