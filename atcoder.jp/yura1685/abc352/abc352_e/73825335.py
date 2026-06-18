from atcoder.dsu import DSU

N, M = map(int,input().split())
CKA = []
for _ in range(M):
    K, C = map(int,input().split())
    A = list(map(int,input().split()))
    CKA.append((C,K,A))
CKA.sort()

groups = N
uf = DSU(N+1)
ans = 0
for C, K, A in CKA:
    S = list(set(uf.leader(a) for a in A))
    ans += (len(S) - 1) * C
    for i in range(len(S)-1):
        uf.merge(S[i], S[i+1])
        groups -= 1

print(ans if groups == 1 else -1)