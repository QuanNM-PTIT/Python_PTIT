def findIdx(n):
    for i in range(1, len(n)):
        if n[i] == n[i - 1]:
            return -1
        if n[i] < n[i - 1]:
            return i
    return -1

def solve(n):
    if len(n) < 3:
        return "NO"
    idx = findIdx(n)
    if idx == -1:
        return "NO"
    for i in range(idx + 1, len(n)):
        if n[i] > n[i - 1]:
            return "NO"
    return "YES"

for i in range(int(input())):
    print(solve(input()))