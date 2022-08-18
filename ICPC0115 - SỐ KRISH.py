t = int(input())

dp = [1]

for i in range(1, 10):
    dp.append(dp[-1] * i)

while t > 0:
    n = input()
    sum = 0
    for i in range(0, len(n)):
        sum += dp[int(n[i])]
    if sum == int(n):
        print("Yes")
    else:
        print("No")
    t -= 1