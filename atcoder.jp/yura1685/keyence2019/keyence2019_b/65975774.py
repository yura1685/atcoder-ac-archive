S = input()

for i in range(7):
    if S[:6-i] + S[-i-1:] == 'keyence':
        print('YES')
        exit()
print('NO')