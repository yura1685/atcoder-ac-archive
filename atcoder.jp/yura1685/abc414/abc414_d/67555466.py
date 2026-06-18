N, M = map(int, input().split())
X = sorted(map(int, input().split()))

if N == M:
    print(0)
    exit()

L = [X[i+1] - X[i] for i in range(N-1)]

L.sort(reverse=True)
ans = (X[-1] - X[0]) - sum(L[:M-1])
print(ans)
