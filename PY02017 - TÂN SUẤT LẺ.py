for i in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    res = a[0]
    for i in a[1:]:
        res ^= i
    print(res)