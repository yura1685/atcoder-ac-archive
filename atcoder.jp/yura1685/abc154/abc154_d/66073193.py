N, K = map(int,input().split())
P = list(map(int,input().split()))

E = 0
s = sum(P[:K])
for i in range(N-K):
    s += - P[i] + P[i+K]
    E = max(E,s)
E = max(E,s)
print((E+K)/2)