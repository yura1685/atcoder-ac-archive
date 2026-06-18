N, X = map(int,input().split())
A = list(map(int,input().split()))
money = 0
for i in range(N):
    if i % 2 == 0:
        money += A[i]
    else:
        money += A[i] - 1
if money <= X:
    print('Yes')
else:
    print('No')