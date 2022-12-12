from string import punctuation

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
    s = input().split()
    tmp = ''
    for j in s:
        for z in j.lower():
            if z.isalnum():
                tmp += z
            else:
                if len(tmp) > 0:
                    if tmp in Dic:
                        Dic[tmp] += 1
                    else:
                        a.append(tmp)
                        Dic[tmp] = 1
                tmp = ''
        if len(tmp) > 0:
            if tmp in Dic:
                Dic[tmp] += 1
            else:
                a.append(tmp)
                Dic[tmp] = 1
        tmp = ''

for j in a:
    arr.append(Data(j, Dic[j]))

arr.sort(key = cmp)

for i in arr:
    print(i.val + ' ' + str(i.f))