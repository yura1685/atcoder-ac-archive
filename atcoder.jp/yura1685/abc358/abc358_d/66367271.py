N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()

if any([B[M-i-1] > A[N-i-1] for i in range(M)]):
    print(-1)
    exit()

money = 0
cnt = 0
for b in B:
    for i in range(cnt, N):
        a = A[i]
        if a >= b:
            money += a
            cnt = i+1
            break

print(money)