N, S = input().split()
N = int(N)
A, T, C, G = [0], [0], [0], [0]

for i in range(N):
    A.append(A[-1]+(S[i]=='A'))
    T.append(T[-1]+(S[i]=='T'))
    C.append(C[-1]+(S[i]=='C'))
    G.append(G[-1]+(S[i]=='G'))

ans = 0
for i in range(1,N):
    for j in range(i+1,N+1):
        if A[j]-A[i-1] == T[j]-T[i-1] and C[j]-C[i-1] == G[j]-G[i-1]:
            ans += 1
print(ans)