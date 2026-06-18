N, M = map(int,input().split())
pair = []
pair2 = []
for m in range(1,N):
    for n in range(m+1,N+1):
        pair.append((m,n))
for photo in range(M):
    a = list(map(int,input().split()))
    for i in range(N-1):
        pair2.append((min(a[i],a[i+1]),max(a[i],a[i+1])))
print(len(pair)-len(set(pair2)))