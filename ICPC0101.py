from operator import le
from typing import List

n = int(input())
a = [int (i) for i in input().split()]
res = []

for i in a:
    if len(res) == 0:
        res.append(i)
    else:
        if (res[-1] + i) % 2 == 0:
            res.pop()
        else:
            res.append(i)

print(len(res))