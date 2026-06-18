A, B, C = map(int,input().split())
A %= B
C %= B
for n in range(1,10**6):
    if (A*n -C) % B == 0:
        print('YES')
        exit()

print('NO')