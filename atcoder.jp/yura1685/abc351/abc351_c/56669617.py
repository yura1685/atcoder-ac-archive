N = int(input())
A = list(map(int,input().split()))

L = []
for i in range(len(A)):
    L.append(A[i])
    while len(L) >= 2:
        c = L[-1]
        if c == L[-2]:
            L.pop()
            L.pop()
            L.append(c+1)
        else:
            break

print(len(L))