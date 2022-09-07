List = list(map(int, input().split()))
b = []

a, K, N = List
i = K - (a % K)

N -= a

while i <= N:
    b.append(i)
    i += K

if (len(b) == 0):
    print(-1)
else:
    for i in b:
        print(i, end = ' ')
