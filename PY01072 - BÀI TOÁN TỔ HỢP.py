n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
l = []

for i in arr:
    if i not in l:
        l.append(i)

l.sort()

n = len(l)
a = []

def Try(idx):
    if len(a) == k:
        for i in a:
            print(i, end = ' ')
        print()
        return
    if idx == n:
        return
    for i in range(idx, len(l)):
        a.append(l[i])
        Try(i + 1)
        a.pop()

Try(0)