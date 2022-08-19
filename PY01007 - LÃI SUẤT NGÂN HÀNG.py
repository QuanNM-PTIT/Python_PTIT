from cmath import log

t = int(input())

while t > 0:
    n, x, m = list(map(float, input().split()))
    x /= 100
    res = log(m / n, 1 + x).real
    if res == int(res):
        print(int(res))
    else:
        print(int(res) + 1)
    t -= 1