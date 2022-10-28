while (True):
    n = int(input())
    if n == 0:
        break
    a = set({})
    a.add(n)
    while n != 1:
        if n & 1 == 1:
            n = n * 3 + 1
        else:
            n >>= 1
        a.add(n)
    print(len(a))