N, L = map(int,input().split())
S = [input()[1::2] for _ in range(L)]
goal = input()[::2].index('o')
amida = [i for i in range(1,N+1)]
for s in S:
    for i in range(N-1):
        if s[i] == '-':
            amida[i], amida[i+1] = amida[i+1], amida[i]

print(amida[goal])