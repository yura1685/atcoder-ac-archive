from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    U, V = map(int, input().split())
    G[U-1].append(V-1)
    G[V-1].append(U-1)

count = defaultdict(int)
cnt = 0
ans = [False] * N

stack = [(0, -1, True)]
while stack:
    u, p, f = stack.pop()
    if f:
        count[A[u]] += 1
        if count[A[u]] == 2:
            cnt += 1
        if cnt > 0:
            ans[u] = True
        stack.append((u, p, False))
        for v in G[u]:
            if v != p:
                stack.append((v, u, True))
    
    else:
        if count[A[u]] == 2:
            cnt -= 1
        count[A[u]] -= 1

for a in ans:
    print('Yes' if a else 'No')