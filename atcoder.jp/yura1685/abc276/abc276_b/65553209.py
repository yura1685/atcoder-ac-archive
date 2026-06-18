N, M = map(int,input().split())
bridge = [[] for i in range(N)]
for i in range(M):
    A, B = map(int,input().split())
    bridge[A-1].append(B)
    bridge[B-1].append(A)
for city in range(N):
    print(len(bridge[city]),end=' ')
    print(*sorted(bridge[city]))