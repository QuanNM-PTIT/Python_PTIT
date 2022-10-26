for i in range(int(input())):
    n = input()
    res1, res2 = 0, 1
    check = False
    for i in range(0, len(n)):
        tmp = ord(n[i]) - ord('0')
        if i & 1 == 0:
            if tmp > 0:
                res2 *= tmp
                check = True
        else:
            res1 += tmp
    if check:
        print(str(res2) + " " + str(res1))
    else:
        print(str(res2) + ' 0')