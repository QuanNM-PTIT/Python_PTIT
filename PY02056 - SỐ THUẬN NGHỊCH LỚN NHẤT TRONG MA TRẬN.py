a = []
c = []

n, m = list(map(int, input().split()))

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
    for j in b:
        x = str(j)
        y = (str(j))[::-1]
        if x == y and len(x) > 1:
            c.append(j)

num = 0

if len(c) == 0:
    print("NOT FOUND")
else:
    num = max(c)
    res = []

    for i in range(n):
        for j in range(m):
            if a[i][j] == num:
                res.append('Vi tri [' + str(i) + '][' + str(j) + ']')
    print(num)
    for i in res:
        print(i)