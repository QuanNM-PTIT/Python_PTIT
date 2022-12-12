m = {}

n = int(input())
a, b = map(int, input().split())

m[a] = 1
m[b] = 1

for i in range(n - 2):
    a, b = map(int, input().split())
    if a in m or b in m:
        if a in m:
            m[a] += 1
        else:
            m[b] += 1
    else:
        break;

def check():
    for i in m.values():
        if i == n - 1:
            return 'Yes'
    return 'No'

print(check())
