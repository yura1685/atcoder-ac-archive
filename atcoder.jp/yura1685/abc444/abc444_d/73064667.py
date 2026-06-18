N = int(input())
A = list(map(int,input().split()))
L = [0] * (max(A)+10)
ans = 0
for a in A:
    L[a] += 1
    i = 0
    while L[a+i] == 10:
        L[a+i] = 0
        L[a+i+1] += 1
        i += 1

L.reverse()
L = map(str,L)
n = int(''.join(L))
print((n-len(A))//9)