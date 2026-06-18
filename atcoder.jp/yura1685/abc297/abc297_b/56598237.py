s = input()
b = 0
for i in range(8):
    if s[i] == 'B':
        b += i
if b % 2 == 0:
    print('No')
    exit()

c = 0
for i in range(8):
    if s[i] == 'K' and c == 0:
        print('No')
        exit()
    if s[i] == 'R':
        c += 1
    if s[i] == 'K' and c == 1:
        print('Yes')
        exit()
print('No')