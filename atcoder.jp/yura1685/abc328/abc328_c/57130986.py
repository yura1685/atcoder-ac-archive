N, Q = map(int,input().split())
S = input()
c = [0]
for i in range(N-1):
    if S[i] == S[i+1]:
        c.append(c[-1]+1)
    else:
        c.append(c[-1])

for i in range(Q):
    l, r = map(int,input().split())
    print(c[r-1] - c[l-1])