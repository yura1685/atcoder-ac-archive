s = list(input())
t = list(reversed(s))
for i in range(len(s)):
    if s[i] == '*' or t[i] == '*':
        pass
    elif s[i] != t[i]:
        print('NO')
        exit()
print('YES')