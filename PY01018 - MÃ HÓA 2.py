p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    inp = input()
    if inp[0] == "0":
        break
    k, s = inp.split()
    k = int(k)
    res = ""
    for i in s:
        res += p[(p.find(i)) % 28]
    print(res[::-1])