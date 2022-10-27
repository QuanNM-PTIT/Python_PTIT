def check(n):
    if len(n) < 3:
        return False
    n = n.lower();
    if n[len(n) - 3:] != '.py':
        return False
    for i in n:
        if ord(i) < ord('a') and ord(i) > ord('z') and ord(i) != ord('.') and ord(i) != ord('_'):
            return False
    return True

#for i in range(int(input())):
n = input()
if check(n):
    print("YES".lower())
else:
    print("NO".lower())