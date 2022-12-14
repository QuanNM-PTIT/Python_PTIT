from datetime import date

file = open('SOTAY.txt', 'r')

s = file.read()

a = []

for i in s.split('\n'):
    if len(i) > 0:
        a.append(i)

class person:
    def __init__(self, d, m, y, hoVaTen, soDienThoai):
        self.d = d
        self.m = m
        self.y = y
        self.hoVaTen = hoVaTen
        l = hoVaTen.split()
        self.ten = l[-1]
        self.hoDem = ''
        for i in range(len(l) - 1):
            self.hoDem += l[i] + ' '
        self.soDienThoai = soDienThoai

    def toString(self):
        return '{}: {} {}/{}/{}'.format(self.hoVaTen, self.soDienThoai, self.d, self.m, self.y)


List = []

dateTime = ''

idx = 0

while idx < len(a):
    if '/' in a[idx]:
        dateTime = a[idx].split()[1]
        idx += 1
    else:
        d, m, y = map(int, dateTime.split('/'))
        List.append(person(d, m, y, a[idx], a[idx + 1]))
        idx += 2


def cmp(a):
    return (a.ten, a.hoDem)


List.sort(key = cmp)

for i in List:
    print(i.toString())