N, M = int(input()), int(input())
F = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    F[a].add(b)
    F[b].add(a)

ans = set(i for i in F[1])
for f in F[1]: ans |= F[f]
print(len(ans)-1 if ans else 0)