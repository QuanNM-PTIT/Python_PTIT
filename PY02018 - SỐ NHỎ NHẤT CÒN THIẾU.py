n = int(input())
a = list(map(int, input().split()))

a.sort()

res = 1

for i in a:
    if i > res:
        break
    elif i == res:
        res += 1

print(res)