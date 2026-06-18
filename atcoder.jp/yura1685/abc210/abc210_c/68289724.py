from collections import defaultdict

N, K = map(int,input().split())
C = list(map(int,input().split()))
d = defaultdict(int)

cnt = 0
for i in range(K):
    if d[C[i]] == 0:
        cnt += 1
    d[C[i]] += 1
ans = cnt

for i in range(N-K):
    d[C[i]] -= 1
    if d[C[i]] == 0:
        cnt -= 1
    d[C[i+K]] += 1
    if d[C[i+K]] == 1:
        cnt += 1
    ans = max(ans,cnt)

print(ans)