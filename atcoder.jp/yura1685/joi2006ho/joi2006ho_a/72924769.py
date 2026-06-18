N, M = map(int,input().split())
cnt = [0] * M
for _ in range(N):
  A = list(map(int,input().split()))
  for i in range(M):
    if A[i]: cnt[i] += 1
ans = [(-cnt[i],i+1) for i in range(M)]
ans.sort()
print(*[X[1] for X in ans])