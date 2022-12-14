import math

def calc(n, k):
    log = int(math.log2(k))
    while k - (1 << log) > 2:
        k -= 1 << log
        log = int(math.log2(k))
    if 1 << log == k:
        return chr(ord('A') + log)
    return chr(ord('A') + k - (1 << log) - 1)

for z in range(int(input())):
    n, k = map(int, input().split())
    print(calc(n, k))
