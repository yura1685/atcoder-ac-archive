s = input()
for i in range(len(s)):
    if s[i] == 'R' and i % 2 == 1:
        print('No');exit()
    if s[i] == 'L' and i % 2 == 0:
        print('No');exit()
print('Yes')