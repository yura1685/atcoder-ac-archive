N, K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9 + 7

Left, Right = [], []
for i in range(N):
    l, r = 0, 0
    for j in range(0,i):
        if A[j] < A[i]:
            l += 1
    for j in range(i+1,N):
        if A[j] < A[i]:
            r += 1
    Left.append(l)
    Right.append(r)

ans = 0
for i in range(N):
    l, r = Left[i], Right[i]
    ans += (K*(K+1)*r + K*(K-1)*l)//2
    ans %= mod

print(ans)