for i in range(int(input())):
    s = input().split()
    cnt = 0
    for j in s:
        if cnt + len(j) <= 100:
            print(j, end = ' ')
            cnt += len(j) + 1
        else:
            break
    print()