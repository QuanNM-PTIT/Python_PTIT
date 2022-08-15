from typing import List

n = int(input())
a = []
a = (input().split())
res = []

for i in a:
    x = int(i)
    if len(res) == 0:
        res.append(x)
    else:
        if(res[-1] + x) % 2 == 0:
            res.pop()
        else:
            res.append(x)

print(len(res))