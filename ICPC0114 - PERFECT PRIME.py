import math

t = int(input())

def isPrime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(math.sqrt(n))
    i = 5
    while i <= sqr:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check(n):
    tmp = int(n)
    sum = 0
    while tmp > 0:
        if isPrime(tmp % 10) == False:
            return False
        sum += tmp % 10
        tmp //= 10
    return isPrime(int(n)) and isPrime(int(n[::-1])) and isPrime(sum)
    
while t > 0:
    n = input()
    if check(n):
        print("Yes")
    else:
        print("No")
    t -= 1
