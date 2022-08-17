import math
from re import T


t = int(input())

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    sqr = math.sqrt(n)
    i = 5
    while i <= sqr:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            cnt += 1
    if(isPrime(cnt)):
        print("YES")
    else:
        print("NO")
    t -= 1
    