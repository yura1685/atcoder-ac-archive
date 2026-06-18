s = input()
t = 'oxxoxxoxxoxx'
if len(s) == 1:
    print('Yes')
    exit()
elif s[0] == 'o':
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')
elif s[0] == 'x' and s[1] == 'x':
    if s == t[1:len(s)+1]:
        print('Yes')
    else:
        print('No')
else:
    if s == t[2:len(s)+2]:
        print('Yes')
    else:
        print('No')