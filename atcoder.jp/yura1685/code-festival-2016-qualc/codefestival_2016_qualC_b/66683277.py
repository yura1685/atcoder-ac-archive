K, T = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)

if K % 2 == 0:
    if M <= K//2:
        print(0)
    else:
        print(2*(M-K//2)-1)
else:
    if M <= (K+1)//2:
        print(0)
    else:
        print(2*(M-K//2-1))