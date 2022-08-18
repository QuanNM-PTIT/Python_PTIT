t = int(input())

while t > 0:
    [n, k] = input().split()
    n, k = int(n), int(k)
    a = list(map(int, input().split()))
    for i in range(k, n):
        print(a[i], end = ' ')
    for i in range(0, k):
        print(a[i], end = ' ')
    print()
    t -= 1
