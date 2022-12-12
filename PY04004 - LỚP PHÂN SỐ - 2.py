import math

class fract:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def reduce(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
        return self

    def add(self, a):
        mau = self.mau * a.mau // math.gcd(self.mau, a.mau)
        res = fract(self.tu * mau // self.mau + a.tu * mau // a.mau, mau)
        return res.reduce()

a, b, c, d = map(int, input().split())

A = fract(a, b)
B = fract(c, d)

C = A.add(B)

print(str(C.tu) + '/' + str(C.mau))