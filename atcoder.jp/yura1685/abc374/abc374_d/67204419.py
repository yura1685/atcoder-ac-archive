from itertools import permutations, product

N, S, T = map(int,input().split())
sen = [tuple(map(int,input().split())) for _ in range(N)]

bas = 0
for A, B, C, D in sen:
    bas += S*((A-C)**2 + (B-D)**2)**(1/2)

P = list(permutations([i for i in range(N)]))
rev = list(product([0,1],repeat=N))

ans = float('inf')
for p in P:
    for r in rev:
        time = 0
        nowx, nowy = 0, 0
        for i in p:
            if r[i] == 0: # そのままのルート
                time += T*((nowx - sen[i][0])**2 + (nowy - sen[i][1])**2)**(1/2)
                nowx, nowy = sen[i][2], sen[i][3]
            else:
                time += T*((nowx - sen[i][2])**2 + (nowy - sen[i][3])**2)**(1/2)
                nowx, nowy = sen[i][0], sen[i][1]
        ans = min(ans,time)

print((ans+bas)/(S*T))