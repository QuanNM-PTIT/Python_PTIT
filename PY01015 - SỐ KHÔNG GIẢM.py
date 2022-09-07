t = int(input())

def solve(s):
    l = len(s)
    for i in range (1, l):
        if s[i] < s[i - 1]:
            return "NO"
    return "YES"

while t > 0:
    s = input()
    print(solve(s))
    t -= 1
