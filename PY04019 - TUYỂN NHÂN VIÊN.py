class nv:
    def __init__(self, ten, id, tb):
        self.id = id
        self.ten = ten
        self.tb = tb
        if tb < 5:
            self.stt = "TRUOT"
        elif tb < 8:
            self.stt = "CAN NHAC"
        elif tb <= 9.5:
            self.stt = "DAT"
        else:
            self.stt = "XUAT SAC"

a = []

def cmp(x):
    return (x.tb * (-1))

for i in range(int(input())):
    ten = input()
    lt = float(input())
    th = float(input())
    if lt > 10:
        lt /= 10.0
    if th > 10:
        th /= 10.0
    id = ''
    id += 'TS0' + str(i + 1)
    a.append(nv(ten, id, (th + lt) / 2.0))

a.sort(key = cmp)

for i in a:
    print(i.id + ' ' + i.ten + ' ' + str.format('{:.2f}', i.tb) + ' ' + i.stt)