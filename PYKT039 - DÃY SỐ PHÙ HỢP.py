def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(check(a, b, n))