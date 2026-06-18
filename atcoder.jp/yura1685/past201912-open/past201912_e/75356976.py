N, Q = map(int, input().split())

follow = [[False] * N for _ in range(N)]
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        a, b = int(q[1]) - 1, int(q[2]) - 1
        follow[a][b] = True
    if q[0] == '2':
        a = int(q[1]) - 1
        for b in range(N):
            if follow[b][a]:
                follow[a][b] = True
    if q[0] == '3':
        a = int(q[1]) - 1
        s = set()
        for b in range(N):
            if follow[a][b]:
                for c in range(N):
                    if follow[b][c]:
                        s.add(c)
        s.discard(a)
        for b in s:
            follow[a][b] = True

ans = [['Y' if F[i] else 'N' for i in range(N)] for F in follow]
for a in ans:
    print(''.join(a))