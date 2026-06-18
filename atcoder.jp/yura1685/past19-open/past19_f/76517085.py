from collections import defaultdict, deque

N = int(input())
d = defaultdict(list)
X, Y = input().split()
for _ in range(N):
    S, T = input().split()
    d[S].append(T)

dq = deque([X])
visit = defaultdict(bool)

while dq:
    u = dq.popleft()
    for v in d[u]:
        if not visit[v]:
            dq.append(v)
            visit[v] = True

print('Yes' if visit[Y] else 'No')