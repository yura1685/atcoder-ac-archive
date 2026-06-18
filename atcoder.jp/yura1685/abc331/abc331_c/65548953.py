import bisect

N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
C = sorted(list(set(A)))

S = {}
for i in range(len(C)):
    x = C[len(C)-1-i]
    if i == 0:
        S[x] = 0
    else:
        y = C[len(C)-i]
        S[x] = S[y] + y*(bisect.bisect(B,y)-bisect.bisect_left(B,y))
c = [S[i] for i in A]
print(*c)