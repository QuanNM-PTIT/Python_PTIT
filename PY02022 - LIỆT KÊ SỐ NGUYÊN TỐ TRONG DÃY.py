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

n = int(input())
a = list(map(int, input().split()))
myMap = {}

for i in a:
    if i not in myMap:
        if isPrime(i):
            myMap[i] = 1
    else:
        myMap[i] += 1

for i in a:
    if i in myMap and myMap[i] > 0:
        print(i, myMap[i])
        myMap[i] = 0