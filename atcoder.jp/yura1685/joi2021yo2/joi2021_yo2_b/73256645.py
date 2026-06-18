from collections import deque

N, Q = map(int,input().split())

pow3 = [3**i for i in range(N+1)]
M = pow3[N]
dist = [-1] * M
dq = deque()

for a in range(N+1):
    for b in range(N+1-a):
        c = N - a - b
        val = 0
        for i in range(a,a+b):
            val += pow3[N-1-i]
        for i in range(a+b,N):
            val += pow3[N-1-i] * 2
        dist[val] = 0
        dq.append(val)

while dq:
    s = dq.popleft()
    d = dist[s]
    for i in range(2,N+1):
        pref = s // pow3[N-i]
        suff = s %  pow3[N-i]
        revp = 0
        tmp = pref
        for _ in range(i):
            revp = revp * 3 + (tmp % 3)
            tmp //= 3
        
        t = revp * pow3[N-i] + suff
        if dist[t] == -1:
            dist[t] = d + 1
            dq.append(t)

dict = {'A':0, 'B':1, 'C':2}
for _ in range(Q):
    S = input()
    S3 = 0
    for i in range(N):
        S3 += dict[S[i]] * pow3[N-1-i]
    print(dist[S3])