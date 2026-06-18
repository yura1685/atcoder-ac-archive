N = int(input())
P = [int(x)-1 for x in input().split()]
ans = []

for i in range(0,N,2):
    if (P[i] + i) % 2 == 0:
        continue
    for j in range(i,1,-2):
        if (P[j-2] + j - 2) % 2 == 0:
            ans.append(('B', j-1))
            P[j], P[j-2] = P[j-2], P[j]
        else:
            break

for i in range(1,N,2):
    if (P[i] + i) % 2 == 0:
        continue
    for j in range(i,2,-2):
        if (P[j-2] + j) % 2 == 0:
            ans.append(('B', j-1))
            P[j], P[j-2] = P[j-2], P[j]
        else:
            break

for i in range(N-1):
    if (P[i] + i) % 2 == 0: continue
    P[i], P[i+1] = P[i+1], P[i]
    ans.append(('A', i+1))

Q = [-1] * N
for i in range(N): Q[P[i]] = i

for i in range(N):
    if Q[i] == i: continue
    n = Q[i] 
    for j in range(n-2,i-1,-2):
        ans.append(('B', j+1))
        Q[P[j]], Q[P[j+2]] = Q[P[j+2]], Q[P[j]]
        P[j], P[j+2] = P[j+2], P[j]

print(len(ans))
for a, n in ans: print(a, n)