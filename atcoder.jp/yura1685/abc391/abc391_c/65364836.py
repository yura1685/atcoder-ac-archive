N, Q = map(int,input().split())

nest = [1]*(N+1)
now  = [i for i in range(0,N+1)]
lovelovesex = 0

for _ in range(Q):
    q = input()
    if q == "2":
        print(lovelovesex)
    else:
        P, H = map(str,q[2:].split())
        p, h = int(P), int(H)
        if nest[now[p]] == 2:
            lovelovesex -= 1
        nest[now[p]] -= 1
        now[p] = h
        if nest[h] == 1:
            lovelovesex += 1
        nest[h] += 1
        