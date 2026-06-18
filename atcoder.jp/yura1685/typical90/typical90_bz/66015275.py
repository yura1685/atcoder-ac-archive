N, M = map(int,input().split())
L = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    if a < b:
        a, b = b, a
    L[a] += 1

print(L.count(1))