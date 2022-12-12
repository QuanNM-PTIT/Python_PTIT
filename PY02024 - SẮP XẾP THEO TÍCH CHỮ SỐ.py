class number:
    def __init__(self, val):
        self.val = val
        self.volDigit = 1
        while val > 0:
            self.volDigit *= val % 10
            val //= 10

def cmp(a):
    return (a.volDigit, a.val)

for z in  range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    l = []
    for i in a:
        l.append(number(i))
    l.sort(key = cmp)
    for i in l:
        print(i.val, end = ' ')
    print()