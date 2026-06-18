N = int(input())

if N % 3 == 0:
    print(-1)
    exit()
if N % 2 == 1:
    print(-1)
    exit()

B = 1
while 5**B < N:
    A = 1
    while 3**A + 5**B < N:
        A += 1
    if 3**A + 5**B == N:
        print(A,B)
        exit()
    B += 1
print(-1)