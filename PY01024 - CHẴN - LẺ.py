def check(s):
    sum = int(s[0])
    for i in range (1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return "NO"
        sum += int(s[i])
    if sum % 10 == 0:
        return "YES"
    return "NO"

for i in range(int(input())):
    s = input()
    print(check(s))