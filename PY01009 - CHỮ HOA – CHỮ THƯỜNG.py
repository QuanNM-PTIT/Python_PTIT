from curses.ascii import isupper

s = input()

upper = 0

for i in range(0, len(s)):
    if s[i].isupper():
        upper += 1

lower = len(s) - upper

if(lower >= upper):
    print(s.lower())
else:
    print(s.upper())