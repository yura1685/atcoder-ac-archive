N = int(input())
K = list(map(int,input().split()))
S = sum(K)
ans = 10**10

for bit in range(1 << N-1):
    hoge = 0
    for i in range(N-1):
        if bit & (1 << i):
            hoge += K[i]
    ans = min(ans, max(hoge,S-hoge))

print(ans)