text = []

while True:
    try:
        text += input().split()
    except Exception:
        break

for i in range(len(text)):
    text[i] = text[i].lower()

s = ''

def check(s):
    if len(s) > 0:
        for i in s:
            if i.isalnum():
                return True;
    return False

for i in text:
    if i[-1] in '.?!':
        tmp = i.split('.')
        tmp = tmp[0].split('?')
        tmp = tmp[0].split('!')
        s += tmp[0]
        if check(s):
            print(s[0].upper() + s[1:])
        s = ''
    else:
        s += i + ' '

if check(s):
    print(s[0].upper() + s[1:])
