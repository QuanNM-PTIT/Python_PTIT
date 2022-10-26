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

def check (n):
    sum = 0
    for i in range(0, len(n)):
        tmp = ord(n[i]) - ord('0')
        if i & 1 == 1 and tmp & 1 == 0:
            return False
        elif i & 1 == 0 and tmp & 1 == 1:
            return False
        sum += tmp
    return isPrime(sum)

for i in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")