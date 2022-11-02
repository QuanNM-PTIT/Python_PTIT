a = []

n, m = list(map(int, input().split()))

Min, Max = 100000, 0

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
    Min = min(Min, min(b))
    Max = max(Max, max(b))

num = Max - Min
res = []

for i in range(n):
    for j in range(m):
        if a[i][j] == num:
            res.append('Vi tri [' + str(i) + '][' + str(j) + ']')

if len(res) == 0:
    print("NOT FOUND")
else:
    print(num)
    for i in res:
        print(i)