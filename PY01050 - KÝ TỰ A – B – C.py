def Try(s, l, a, b, c):
    if len(s) == l:
        if a <= b and b <= c and a > 0:
            print(s)
        return
    if len(s) < l:
        Try(s + "A", l, a + 1, b, c)
        Try(s + "B", l, a, b + 1, c)
        Try(s + "C", l, a, b, c + 1)

n = int(input())
for i in range(3, n + 1):
    Try("", i, 0, 0, 0)