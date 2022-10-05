num = []

def check(n):
    for i in n:
        if int(i) & 1 == 1:
            return False
    return n == n[::-1]

def add(start, end):
    for i in range(start, end, 2):
        if (check(str(i))):
            num.append(i)

add(22, 100)
add(1000, 10000)
add(100000, 1000000)

def solve(n):
    n = int(n)
    for i in num:
        if (i >= n):
            break
        print(i, end = ' ')
    print()

for i in range(int(input())):
    solve(input())