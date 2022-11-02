n = int(input())
a = []
b = []

while len(a) < n:
    a += list(map(int, input().split()))

for i in range(1, a[-1] + 1):
    if i not in a:
        b.append(i)

if len(b) == 0:
    print("Excellent!")
else:
    for i in b:
        print(i)