N = int(input())
d = {}
for _ in range(N):
    S = input()
    if d.get(S) == None:
        d[S] = 1
        print(S)
    else:
        print(S+'('+str(d[S])+')')
        d[S] += 1