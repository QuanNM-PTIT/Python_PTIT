s = input()

s = s[::-1]
res = ""
cnt = 0

for i in s:
    if cnt == 3:
        res += ','
        cnt = 0
    res += i
    cnt += 1

print(res[::-1])