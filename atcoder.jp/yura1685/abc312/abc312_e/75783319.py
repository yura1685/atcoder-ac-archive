N = int(input())
S = [[[-1] * 100 for _ in range(100)] for _ in range(100)]
for i in range(N):
    X1, Y1, Z1, X2, Y2, Z2 = map(int, input().split())
    for x in range(X1, X2):
        for y in range(Y1, Y2):
            for z in range(Z1, Z2):
                S[x][y][z] = i
ans = [set() for _ in range(N)]
for x in range(100):
    for y in range(100):
        for z in range(100):
            i = S[x][y][z]
            if i == -1: continue
            if x + 1 < 100:
                j = S[x+1][y][z]
                if j != -1 and j != i:
                    ans[i].add(j)
                    ans[j].add(i)
            if y + 1 < 100:
                j = S[x][y+1][z]
                if j != -1 and j != i:
                    ans[i].add(j)
                    ans[j].add(i)
            if z + 1 < 100:
                j = S[x][y][z+1]
                if j != -1 and j != i:
                    ans[i].add(j)
                    ans[j].add(i)

for s in ans:
    print(len(s))