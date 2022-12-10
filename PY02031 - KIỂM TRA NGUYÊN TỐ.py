import math

def isPrime(n):
    if n < 2:
        return 0
    if n < 4:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    sqr = int(math.sqrt(n))
    for i in range (5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return 0
    return 1

n, m = map(int, input().split())

for i in range(n):
    a = list(map(int, input().split()))
    for j in a:
        print(isPrime(j), end = ' ')
    print()

