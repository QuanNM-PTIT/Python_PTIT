for i in range(int(input())):
    sum = 0
    for i in input():
        sum += int(i)
    if str(sum) == str(sum)[::-1] and sum > 9:
        print("YES")
    else:
        print("NO")