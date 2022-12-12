import math

def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(math.sqrt(n))
    for i in range (5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n, m = map(int, input().split())

a = []
maxx = -1

for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
    for j in tmp:
        if isPrime(j) and j > maxx:
            maxx = j

if maxx == -1:
    print('NOT FOUND')
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print('Vi tri [' + str(i) + '][' + str(j) + ']')