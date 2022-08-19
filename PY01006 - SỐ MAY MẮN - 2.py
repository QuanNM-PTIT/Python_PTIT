t = int(input())

def solve(n):
    for i in n:
        if i != '4' and i != '7':
            return "NO"
    return "YES"

while t > 0:
    n = input()
    print(solve(n))
    t -= 1