N = int(input())
X_in = list(map(int, input().split()))
X = [X_in[i+1] - X_in[i] for i in range(N-1)]

Y = sorted(X[0::2])
Z = sorted(X[1::2])

L = []
for i in range(len(Z)):
    L.append(Y[i])
    L.append(Z[i])
if N % 2 == 0:
    L.append(Y[-1])

ans = X_in[0]
sum = X_in[0]
for x in L:
    sum += x
    ans += sum
    
print(ans)