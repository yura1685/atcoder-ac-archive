N, M = map(int, input().split())
Q = []
for _ in range(M):
    k = int(input())
    L = []
    for _ in range(k):
        a, b = map(int, input().split())
        L.append((a-1, b))
    Q.append(L)

for n in range(1 << N):
    for L in Q:
        for a, b in L:
            if n >> a & 1 == b:
                break
        else:
            break
    else:
        print('Yes')
        break
else:
    print('No')