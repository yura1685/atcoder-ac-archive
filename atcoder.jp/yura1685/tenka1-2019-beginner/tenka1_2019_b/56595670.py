n = int(input())
s = list(input())
r = s[int(input())-1]
for i in range(n):
    if s[i] != r:
        s[i] = '*'
print(''.join(s))