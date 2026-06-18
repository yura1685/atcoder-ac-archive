N, M = map(int,input().split())
B = []
nex = []
whe = [-1] * (N+1)
for i in range(M):
    k = int(input())
    A = list(map(int,input().split()))
    A.reverse()
    B.append(A)
    a = A[-1]
    if whe[a] == -1:
        whe[a] = i
    else:
        nex.append((whe[a],i))

cnt = 0
while nex:
    i, j = nex.pop()
    B[i].pop()
    if B[i]:
        b = B[i][-1]
        if whe[b] == -1:
            whe[b] = i
        else:
            nex.append((whe[b],i))
    B[j].pop()
    if B[j]:
        b = B[j][-1]
        if whe[b] == -1:
            whe[b] = j
        else:
            nex.append((whe[b],j))
    cnt += 1


print('Yes' if cnt == N else 'No')