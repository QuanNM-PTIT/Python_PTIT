class student:
    def __init__(self, hoVaTen, soBaiLamDung, soLanSubmit):
        self.hoVaTen = hoVaTen
        self.soBaiLamDung = soBaiLamDung
        self.soLanSubmit = soLanSubmit

a = []

for z in range(int(input())):
    x = input()
    y, z = map(int, input().split())
    a.append(student(x, y, z))

a.sort(key = lambda i : ((-1) * i.soBaiLamDung, i.soLanSubmit, i.hoVaTen))

for i in a:
    print('{} {} {}'.format(i.hoVaTen, i.soBaiLamDung, i.soLanSubmit))