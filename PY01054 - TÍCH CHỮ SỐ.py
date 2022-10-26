for i in range(int(input())):
    n = input()
    res = 1
    for j in n:
        tmp = ord(j) - ord('0')
        if tmp > 0:
            res *= tmp
    print(res)
