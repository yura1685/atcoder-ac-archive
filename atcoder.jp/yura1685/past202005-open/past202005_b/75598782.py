I = input().split()
N, M, Q = int(I[0]), int(I[1]), int(I[2])
solve = [[] for _ in range(N+1)]
prob = [N] * (M+1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 2:
        n, m = q[1:]
        solve[n].append(m)
        prob[m] -= 1
    
    else:
        ans = 0
        for x in solve[q[1]]:
            ans += prob[x]
        print(ans)