import math
from pickle import TRUE

t = int(input())

isPrime = [1] * 1000005
isPrime[0] = isPrime[1] = 0

for i in range (2, 1000):
    if isPrime[i] == 1:
        j = i * i
        while j <= int(1e6):
            isPrime[j] = 0
            j += i

while t > 0:
    n = int(input())
    dic = {}
    for i in range(13, n):
        num = int(str(i)[::-1])
        if isPrime[i] == 0 or isPrime[num] == 0 or num >= n or num in dic or i == num:
            continue
        print(i, num, end = ' ')
        dic[num] = dic[i] = 1
    print()
    t -= 1