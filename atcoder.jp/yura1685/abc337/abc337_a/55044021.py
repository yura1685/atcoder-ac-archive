N = int(input())
A, B = 0, 0
for i in range(N):
    X, Y = map(int, input().split())
    A += X
    B += Y
if A == B:
    print('Draw')
elif A < B:
    print('Aoki')
else:
    print('Takahashi')