N = int(input())
A = list(map(int,input().split()))

m4 = 0
m2 = 0

for a in A:
    if a % 4 == 0:
        m4 += 1
    elif a % 2 == 0:
        m2 += 1

if m4 >= N//2:
    print('Yes')
    exit()

left = N - 2*m4
kisu = N-m4-m2

if left <= m2:
    print('Yes')
else:
    print('No')