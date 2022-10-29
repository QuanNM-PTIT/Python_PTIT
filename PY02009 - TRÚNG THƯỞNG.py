class Data:
    def __init__(self, val, f):
        self.val = val
        self.f = f

def cmp(a):
    return (a.f * (-1), a.val)

for i in range(int(input())):
    n = int(input())
    a = []
    b = []
    Dic = {}
    for j in range(n):
        x = int(input())
        if x not in a:
            a.append(x)
            Dic[x] = 0
        else:
            Dic[x] += 1
    for j in a:
        b.append(Data(j, Dic[j]))
    b.sort(key = cmp)
    print(b[0].val)