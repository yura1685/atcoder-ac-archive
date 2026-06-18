N = int(input())
S, T = map(str,input().split())
L = []
for i in range(N):
    L.append(S[i])
    L.append(T[i])
a = ''.join(L)
print(a)