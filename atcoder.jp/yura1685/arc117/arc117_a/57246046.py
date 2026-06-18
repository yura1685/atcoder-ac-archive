A, B = map(int,input().split())
if B < A:
    L = [i for i in range(1,A+1)]
    for i in range(1,B):
        L.append(-i)
    L.append(-sum(L))
elif A < B:
    L = [-i for i in range(1,B+1)]
    for i in range(1,A):
        L.append(i)
    L.append(-sum(L))
else:
    c = [i for i in range(1,A+1)]
    d = [-j for j in range(1,A+1)]
    L = c + d
print(*L)