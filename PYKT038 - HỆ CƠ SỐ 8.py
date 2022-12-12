def change(s):
    res = 0
    for i in range(3):
        if (s[i] == '1'):
            res += 1 << (2 - i)
    return res

n = input()

while len(n) % 3 > 0:
    n = '0' + n

for i in range(0, len(n), 3):
    print(change(n[i : i + 3]), end = '')

