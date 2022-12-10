n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

nuaTren, nuaDuoi = 0, 0

for i in range(n):
    for j in range(n):
        if j > i:
            nuaTren += a[i][j]
        elif j < i:
            nuaDuoi += a[i][j]

if abs(nuaTren - nuaDuoi) <= k:
    print('YES')
else:
    print('NO')

print(abs(nuaTren - nuaDuoi))