class student:
    def __init__(self, ID, name, Class):
        self.ID = ID
        self.name = name
        self.Class = Class
        self.p = 10

    def calc(self, s):
        for i in s:
            if i == 'm':
                self.p -= 1
            elif i == 'v':
                self.p -= 2
        if self.p <= 0:
            self.p = 0

    def prt(self):
        print(self.ID + " " + self.name + " " + self.Class + " " + str(self.p), end = '')
        if self.p == 0:
            print(" KDDK", end = '')
        print()

m = {}
a = []
t = int(input())

for i in range(t):
    tmp = student(input(), input(), input())
    m[tmp.ID] = tmp
    a.append(tmp)

for i in range(t):
    id, status = input().split()
    m[id].calc(status)

for i in a:
    i.prt()

