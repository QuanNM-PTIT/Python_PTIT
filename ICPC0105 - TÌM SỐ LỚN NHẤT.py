from ctypes.wintypes import CHAR

n = int(input())

while n > 0:
    s = input()
    s += "*"
    res = -1
    x = 0
    l = len(s)
    for i in range(0, l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = max(res, x)
                x = 0
    print(max(res, x))
    n -= 1