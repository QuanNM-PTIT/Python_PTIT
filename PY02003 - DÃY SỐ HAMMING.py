myMap = {}
a = []

for i in range(60):
    for j in range(38):
        for z in range(26):
            num = 2 ** i * 3 ** j * 5 ** z
            if num not in myMap:
                myMap[num] = 1
                a.append(num)

a.sort()


def binSearch(l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid + 1
        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1


for i in range(int(input())):
    n = int(input())
    idx = binSearch(0, len(a) - 1, n)
    if idx == -1:
        print("Not in sequence")
    else:
        print(idx)
