a = []
Dic = {}
arr = []

class Data:
    def __init__(self, val, f):
        self.val = val
        self.f = f

def cmp(a):
    return (a.f * (-1), a.val)

for i in range(int(input())):
    s = input()
    s = s.lower()
    tok = ',.?!:;/-()'
    for j in tok:
        s = s.replace(j, ' ')
    tmp = s.split()
    for j in tmp:
        if j in a:
            Dic[j] += 1
        else:
            a.append(j)
            Dic[j] = 1

for j in a:
    arr.append(Data(j, Dic[j]))

arr.sort(key = cmp)

for i in arr:
    print(i.val + ' ' + str(i.f))