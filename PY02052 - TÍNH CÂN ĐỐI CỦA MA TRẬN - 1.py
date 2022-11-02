a = []

n = int(input())

for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

tren, duoi = 0, 0

for i in range(n):
    for j in range(n):
        if j > i:
            tren += a[i][j]
        elif j < i:
            duoi += a[i][j]

if abs(tren - duoi) <= k:
    print("YES")
else:
    print("NO")
print(abs(tren - duoi))