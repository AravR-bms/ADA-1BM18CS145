arr = ["1011", "0111", "0101", "1100", "1101"]
res = 0

# for number in arr:
#     print(int(number, 2))

for number in arr:
    if number.count("1") % 2 == 0:
        print(number)
        res += int(number, 2)

print(res)
