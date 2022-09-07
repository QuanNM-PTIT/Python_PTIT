from math import sqrt


t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(sqrt(n)) + 1
    for i in range(5, sqr, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def sumDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


while t > 0:
    List = list(map(int, input().split()))
    a, b = List
    if isPrime(sumDigit(gcd(a, b))):
        print("YES")
    else:
        print("NO")
    t -= 1