from curses.ascii import isalpha

def solve(a):
    for i in a:
        if isalpha(i):
            return "NO"
        x = int(i)
        if x != 0 and x != 1 and x != 2:
            return "NO"
    return "YES"

for i in range(int(input())):
    print(solve(input()))