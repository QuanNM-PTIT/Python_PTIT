def solve(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(2, len(n)):
        if n[i] != n[i & 1]:
            return "NO"
    return "YES"

for i in range(int(input())):
    print(solve(input()))