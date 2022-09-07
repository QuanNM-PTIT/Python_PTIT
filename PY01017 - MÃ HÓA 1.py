t = int(input())

def solve(s):
    cnt = 1
    l = len(s)
    for i in range(1, l):
        if s[i] != s[i - 1]:
            print(cnt, end = '')
            print(s[i - 1], end = '')
            cnt = 1
        else:
            cnt += 1
    print(cnt, end = '')
    print(s[l - 1])


while t > 0:
    s = input()
    solve(s)
    t -= 1