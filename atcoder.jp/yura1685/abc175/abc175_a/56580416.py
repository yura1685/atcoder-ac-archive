s = input()
if s[1] != 'R':
    if 'R' in s:
        print(1)
    else:
        print(0)
else:
    print(s.count('R'))    