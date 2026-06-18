N, M = map(int,input().split())

man = [tuple(map(int,input().split())) for _ in range(N)]
check = [tuple(list(map(int,input().split()))+[i+1]) for i in range(M)]

def dis(P,Q):
    return abs(P[0]-Q[0]) + abs(P[1]-Q[1]), Q[2]

ans = []
for m in man:
    d, point = 10**10, 0
    for p in check:
        a, b = dis(m,p)
        if a < d:
            d, point = a, b
    ans.append(point)

for i in ans:
    print(i)