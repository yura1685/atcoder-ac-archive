N, M = map(int,input().split())
A = list(map(int,input().split()))

j = 0
B = A[:M]
S = sum(B)

ans = 0
for i in range(M):
    ans += (i+1)*B[i]
last = ans

for j in range(1,N-M+1):
    c = last
    c += -S + M*A[M+j-1]
    ans = max(c,ans)
    S += A[M+j-1] - A[j-1]
    last = c

print(ans)
