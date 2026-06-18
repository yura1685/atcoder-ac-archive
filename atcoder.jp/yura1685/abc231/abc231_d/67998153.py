from atcoder.dsu import DSU

N, M = map(int,input().split())
dsu = DSU(N)

cnt = [0]*N

for _ in range(M):
    A, B = map(int,input().split())
    A, B = A-1, B-1
    if dsu.same(A,B):
        exit(print('No'))
    dsu.merge(A,B)
    cnt[A] += 1
    cnt[B] += 1

print('Yes' if max(cnt) < 3 else 'No')