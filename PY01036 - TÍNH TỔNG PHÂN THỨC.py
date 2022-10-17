for i in range (int(input())):
    n = int(input())
    res = 0.0
    if n & 1 == 1:
        for j in range(1, n + 1, 2):
            res += 1.0 / j
    else:
        for j in range(2, n + 1, 2):
            res += 1.0 / j
    print("{:.6f}".format(res))