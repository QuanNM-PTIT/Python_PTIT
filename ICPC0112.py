import math

t = int(input())

isPrime = [1] * 1000005
isPrime[0] = isPrime[1] = 0

for i in range (2, 1000):
    if isPrime[i] == 1:
        j = i * i
        while j <= int(1e6):
            isPrime[j] = 0
            j += i

Prime = []

for i in range(2, int(1e6)):
    if isPrime[i] == 1:
        Prime.append(i)

while t > 0:
    n = int(input())
    cnt = 0
    idx = 0
    while Prime[idx] <= n - 6:
        num = Prime[idx]
        if isPrime[num + 6] == 1 and (isPrime[num + 2] == 1 or isPrime[num + 4] == 1):
            cnt += 1
        idx += 1
    print(cnt)
    t -= 1
