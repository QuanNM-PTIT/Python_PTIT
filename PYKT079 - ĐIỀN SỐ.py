for i in range(int(input())):
    n = input()
    a = list(set(map(int, input().split())))
    a.sort()
    print(a[-1] - a[0] - len(a) + 1)

