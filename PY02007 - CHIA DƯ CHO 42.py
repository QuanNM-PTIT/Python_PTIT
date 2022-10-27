a = []

while len(a) < 10:
    a += list(map(int, input().split()))

for i in range(len(a)):
    a[i] %= 42

print(len(set(a)))