root = [i for i in range(305)]

def findRoot(x):
    if x == root[x]:
        return x
    root[x] = findRoot(root[x])
    return root[x]

def union(x, y):
    rootX = findRoot(x)
    rootY = findRoot(y)
    root[rootX] = rootY

n, m, x = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

x = findRoot(x)

for i in range(1, n + 1):
    if findRoot(i) != findRoot(x):
        print(i)
