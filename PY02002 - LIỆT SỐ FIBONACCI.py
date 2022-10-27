fibo = [0, 1, 1]

for i in range(3, 93):
    fibo.append(fibo[i - 1] + fibo[i - 2])

for i in range(int(input())):
    l, r = list(map(int, input().split()))
    for j in range(l, r + 1):
        print(fibo[j], end = ' ')
    print()