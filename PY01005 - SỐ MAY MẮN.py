n = input()

cnt = 0

for i in n:
    if i == '4' or i == '7':
        cnt += 1

if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")