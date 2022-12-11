root = [i for i in range(100005)]

def findRoot(x):
    if x == root[x]:
        return x
    root[x] = findRoot(root[x])
    return root[x]

def check(x, y):
    rootX = findRoot(x)
    rootY = findRoot(y)
    if rootX == rootY:
        return 1
    return 0

def union(x, y):
    rootX = findRoot(x)
    rootY = findRoot(y)
    root[rootX] = rootY

for i in range(int(input())):
    x, y, z = map(int, input().split())
    if z == 1:
        union(x, y)
    else:
        print(check(x, y))
