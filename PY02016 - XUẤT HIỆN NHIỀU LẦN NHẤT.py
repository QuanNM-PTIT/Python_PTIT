for z in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    myMap = {}
    fMax = 1
    num = int(1e7)
    for i in a:
        if i not in myMap:
           myMap[i] = 1
        else:
            myMap[i] += 1
    fMax = max(myMap.values())
    for f, s in myMap.items():
        if s == fMax:
            fMax = s
            num = min(num, f)
    if (fMax > n // 2):
        print(num)
    else:
        print('NO')