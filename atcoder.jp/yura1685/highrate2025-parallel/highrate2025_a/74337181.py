N, M = map(int, input().split())
ans = []
for i in range(1, N+1):
    S, E = map(int, input().split())
    ans.append((S*M+E, i))
ans.sort()
for t, i in ans:
    print(i)