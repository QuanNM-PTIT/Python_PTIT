t = int(input())

def solve(s):
    l = len(s)
    for i in range(1, l, 2):
        cnt = int(s[i])
        for j in range(cnt):
            print(s[i - 1], end = '')
    print()

while t > 0:
    s = input()
    solve(s)
    t -= 1