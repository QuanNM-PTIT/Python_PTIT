delim = '.!?'

a = []

while True:
    try:
        s = input()
        s = s.lower()
        s = s.strip()
        x = ''
        for i in s:
            if i in delim:
                x = x.strip()
                if len(x) > 0:
                    x += i
                    a.append(x)
                x = ''
            else:
                x += i
        x = x.strip()
        if len(x) > 0:
            a.append(x)
    except Exception:
        break

for i in a:
    s = i.split()
    res = ''
    for j in s:
        if len(j) > 0:
            res += j + ' '
    res = res[:len(res) - 1]
    if res[-1] not in delim:
        res += '.'
    res = res.capitalize()
    print(res)