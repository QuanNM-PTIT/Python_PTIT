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

prime = [2]

for i in range(3, 8000, 2):
    if isPrime(i):
        prime.append(i)

n, x = list(map(int, input().split()))

print(x, end = ' ')
for i in range(n):
    print(x + prime[i], end = ' ')
    x = x + prime[i]