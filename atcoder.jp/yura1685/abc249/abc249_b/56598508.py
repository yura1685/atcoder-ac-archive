s = input()
a = s
c = 0
for i in range(len(s)):
    if a[i] != s[i].upper():
        break
    else:
        c += 1
if c == len(s):
    print('No')
    exit()

c = 0
for i in range(len(s)):
    if a[i] != s[i].lower():
        break
    else:
        c += 1
if c == len(s):
    print('No')
    exit()

if len(set(a)) != len(a):
    print('No')
    exit()

print('Yes')