N, M = map(int,input().split())
cnt = [[] for _ in range(M+1)]
for _ in range(N):
    a, b = map(int,input().split())
    cnt[a].append(b)

for i in range(1,M+1):
    print(sum(cnt[i])/len(cnt[i]))